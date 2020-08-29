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
import Level.IMU as IMU
import time

class myLevel(threading.Thread):
    """Documentationuse the berryIMU to measure inclination"""
    def __init__(self,zeroX,zeroY):
        super(myLevel, self).__init__()
        
        IMU.detectIMU()     #Detect if BerryIMU is connected.
        if(IMU.BerryIMUversion == 99):
            print(" No BerryIMU found... exiting ")
            sys.exit()
        IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass

        self.zeroX = zeroX
        self.zeroY = zeroY

        self.data = {}
        self.newData = signal("Level")
        self.Doit    = True

    ## --------------------------------------------------------------
    ## Description : run
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-53-2020 14:53:16
    ## --------------------------------------------------------------
    def run(self):
        while self.Doit:
            self.data.clear()
            [self.data["X"],self.data["Y"]] = self.measure(100)
            self.newData.send(self.data)
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
