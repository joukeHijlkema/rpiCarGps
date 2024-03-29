#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 17:29 2017
#   - Initial Version 1.0
#  =================================================
import threading
# from gps3 import gps3
from gps3.agps3threaded import AGPS3mechanism
from blinker import signal
import time
import arrow
import random
import os

class Gps(threading.Thread):
    data    = {}
    init=True
    def __init__(self,real):
        "listen to gps data and emit some if anything new arrives"
        super(Gps, self).__init__()

        self.test = not real
        
        # self.gps_socket = gps3.GPSDSocket()
        # self.data_stream = gps3.DataStream()
        # self.gps_socket.connect()
        # self.gps_socket.watch()
        self.agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
        self.agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
        
        self.newData = signal('Gps')
        self.Doit    = True
        self.init    = True

        self.dummyLat = 43.168583333
        self.dummyLon = 1.191853333
        print("GPS init done")
        
    ## --------------------------------------------------------------
    ## Description :run
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 17-52-2017 18:52:05
    ## --------------------------------------------------------------
    def run (self):
        print("Start GPS thread")
        if self.test==True:
            print("test run")
            self.init=False
            while self.Doit:
                self.data.clear()
                self.data['speed'] = random.randrange(0,100,1)
                self.data['time']  = arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")
                self.dummyLon+=0.001
                self.dummyLat+=0.001
                self.data['lon']   = self.dummyLon
                self.data['lat']   = self.dummyLat
                self.data['alt']    = random.randrange(0,1000,1)
                self.data['climb']  = random.randrange(-10,10,1)
                self.newData.send(self.data)
                time.sleep(1)
        else:
            self.agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths of a second
            while self.Doit:
                self.data.clear()
                if self.init == True:
                    if self.agps_thread.data_stream.time != "n/a":
                        try:
                            os.system("sudo date -s %s"%self.agps_thread.data_stream.time)
                            self.init=False
                        except:
                            print("waiting for time")
                else:
                    self.data["time"]  = self.agps_thread.data_stream.time
                    self.data["speed"] = self.agps_thread.data_stream.speed
                    self.data["lon"]   = self.agps_thread.data_stream.lon
                    self.data["lat"]   = self.agps_thread.data_stream.lat
                    self.data["alt"]   = self.agps_thread.data_stream.alt
                    self.data["climb"] = self.agps_thread.data_stream.climb
                    self.newData.send(self.data)

                time.sleep(1)
        print("myGps quited")
    
if __name__ == '__main__':

    import cProfile
    ## --------------------------------------------------------------
    ## Description : echo GPS data
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 30-03-2020 17:03:27
    ## --------------------------------------------------------------
    def gotGpsData(data):
        print("=== GPS Data ===")
        for i in data:
            print("| %s: %s"%(i,data[i]))

    myGps = Gps(True)
    # cProfile.run("myGps.run()")
    myGps.start()
    gpsData = signal('Gps')
    gpsData.connect(gotGpsData)

    cmd = input("Press key to quit")

    myGps.Doit=False
    
