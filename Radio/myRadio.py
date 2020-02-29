#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 21:51 2019
#   - Initial Version 1.0
#  =================================================
import time
import threading
from blinker import signal

# from Classes.myTea5767 import myTea5767 as myTuner
from Classes.mySi4703 import mySi4703 as myTuner

class myRadio(threading.Thread):
    """Documentation for myRadio

    """
    def __init__(self,lastFreq,i2c_address=0x60,i2c_bus=1):
        super(myRadio, self).__init__()
        
        self.tuner    = myTuner(i2c_address,i2c_bus)
        self.lastFreq = lastFreq
        self.Doit     = True

        self.fromRadio = signal('fromRadio')
        self.toRadio   = signal('toRadio')
        self.toRadio.connect(self.incommingSignal)
        tunerData      = signal('Tuner')
        tunerData.connect(self.newTunerData)

    ## --------------------------------------------------------------
    ## Desc : 
    ## -
    ## Author : jouke hylkema
    ## date   : 26-36-2019 12:36:42
    ## --------------------------------------------------------------
    def run (self):
        self.Doit = True
        self.tuner.setFrequency(self.lastFreq)
        while self.Doit:
            time.sleep(1)

        self.tuner.Quit()
        print("closed")
        
    ## --------------------------------------------------------------
    ## Description : new tuner data arrived
    ## NOTE : just send it through 
    ## -
    ## Author : jouke hylkema
    ## date   : 26-11-2019 13:11:03
    ## --------------------------------------------------------------
    def newTunerData (self,data):
        print("new data from tuner")
        self.fromRadio.send(data)

    ## --------------------------------------------------------------
    ## Description : treat recevieved signal
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 28-44-2019 11:44:29
    ## --------------------------------------------------------------
    def incommingSignal (self,data):
        if "seekUp" in data:
            self.tuner.search(1)
        elif "seekDown" in data:
            self.tuner.search(0)
        

if __name__ == '__main__':

    import sys
    sys.path

    def printData(data):
        for d in data:
            if type(data[d]) is list:
                out = "".join(data[d]).strip()
            else:
                out = data[d]
            print("%s: %s"%(d,out))

    signal("fromRadio").connect(printData)
    
    r = myRadio(87.9,0x10,1)
    r.start()
    
    while 1:
        cmd = input("Press key (u=search up, d=search down, s:f=set freq, q=quit): ").lower()
        if "q" in cmd:
            r.Doit = False
            print("quitting")
            break
        elif "s" in cmd:
            f = float(cmd.split(":")[1])
            r.tuner.setFrequency(f)
        elif "u" in cmd:
            r.tuner.search(1)
        elif "d" in cmd:
            r.tuner.search(0)

    time.sleep(2)
