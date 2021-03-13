#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 14:23 2020
#   - Initial Version 1.0
#  =================================================
import threading
from blinker import signal
import IMU as IMU
import time
import sys

class myLevel(threading.Thread):
    """Documentationuse the berryIMU to measure inclination"""
    def __init__(self,zeroX,zeroY):
        super(myLevel, self).__init__()
        
        IMU.detectIMU()     #Detect if BerryIMU is connected.
        if(IMU.BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            # sys.exit()
            self.Doit = False
            return
        IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass

        self.zeroX = zeroX
        self.zeroY = zeroY

        self.data = {}

        self.fromLevel = signal("fromLevel")
        self.toLevel   = signal("toLevel")
        self.toLevel.connect(self.messageReceived)

        self.Measure = False
        self.Doit    = True

    ## --------------------------------------------------------------
    ## Description : treat incomming signal
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-04-2020 16:04:08
    ## --------------------------------------------------------------
    def messageReceived(self, msg):
        if "start" in msg:
            self.Measure = True
        elif "stop" in msg:
            self.Measure = False
        elif "reset" in msg:
            self.raz()
    ## --------------------------------------------------------------
    ## Description : run
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-53-2020 14:53:16
    ## --------------------------------------------------------------
    def run(self):
        while self.Doit:
            if self.Measure:
                self.data.clear()
                [self.data["X"],self.data["Y"]] = self.measure(100)
                self.fromLevel.send(self.data)
            time.sleep(1)
            
    ## --------------------------------------------------------------
    ## Description : read N measures and return the average
    ## NOTE : I think the range for +/- 90° ~ +/- 4200
    ## -
    ## Author : jouke hylkema
    ## date   : 29-37-2020 14:37:30
    ## --------------------------------------------------------------
    def measure(self, N):
        X = 0
        Y = 0
        for i in range(N):
            X+=IMU.readACCx()
            Y+=IMU.readACCy()
        return [(X/N)-self.zeroX,(Y/N)-self.zeroY]

    ## --------------------------------------------------------------
    ## Description : raz
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-44-2020 14:44:41
    ## --------------------------------------------------------------
    def raz(self):
        self.zeroX = 0
        self.zeroY = 0

        [self.zeroX,self.zeroY] = self.measure(500)
        self.fromLevel.send(["raz",self.zeroX,self.zeroY])

if __name__ == '__main__':

    ## --------------------------------------------------------------
    ## Description : echo data
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 30-03-2020 17:03:27
    ## --------------------------------------------------------------
    def gotData(data):
        print("=== LEVEL Data ===")
        for i in data:
            print("| %s: %s"%(i,data[i]))

    Level = myLevel(0,0)
    Level.start()
    signal('fromLevel').connect(gotData)
    Level.toLevel.send("start")

    cmd = input("Press key to quit")

    Level.Doit=False
    
       
