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
import gps
from blinker import signal
import time
import arrow
import random

class Gps(threading.Thread):
    data    = {}
    def __init__(self,real):
        "listen to gps data and emit some if anything new arrives"
        super(Gps, self).__init__()

        self.test = not real
        
        # Listen on port 2947 (gpsd) of localhost
        self.session  = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        self.newData  = signal('Gps')
        self.Doit     = True

        self.dummyLat = 43.168583333
        self.dummyLon = 1.191853333
        
    ## --------------------------------------------------------------
    ## Description :run
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 17-52-2017 18:52:05
    ## --------------------------------------------------------------
    def run (self):
        if self.test==True:
            print "test run"
            while self.Doit:
                self.data.clear()
                self.data['speed'] = random.randrange(0,100,1)
                self.data['time']  = arrow.now().format("YY-MM-DD HH:mm:ss")
                self.dummyLon+=0.001
                self.dummyLat+=0.001
                self.data['lon']   = self.dummyLon
                self.data['lat']   = self.dummyLat
                self.newData.send(self.data)
                time.sleep(1)
        else:
            while self.Doit:
                try:
                    report = self.session.next()
                    # Wait for a 'TPV' report and display the current time
                    # To see all report data, uncomment the line below
                    # print(report)
                    if report['class'] == 'TPV':
                        self.data.clear()
                        for i in ['time','speed','lon','lat']:
                            if hasattr(report, i):
                                exec("self.data['{0}']=report.{0}".format(i))
                        self.newData.send(self.data)
                except KeyError:
                    pass
                except KeyboardInterrupt:
                    quit()
                except StopIteration:
                    self.session = None
    
