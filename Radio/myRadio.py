#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 21:51 2019
#   - Initial Version 1.0
#  =================================================
# Gstreamer to redirect sound to the amp
import time
import threading
from blinker import signal

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
        # print("new data from tuner")
        self.fromRadio.send(data)

    ## --------------------------------------------------------------
    ## Description : treat recevieved signal
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 28-44-2019 11:44:29
    ## --------------------------------------------------------------
    def incommingSignal (self,data):
        self.tuner.clearData()
        if "seekUp" in data:
            self.tuner.search(1)
        elif "seekDown" in data:
            self.tuner.search(0)

    ## --------------------------------------------------------------
    ## Description : return the actual frequency
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-26-2021 17:26:53
    ## --------------------------------------------------------------
    def getFreq(self):
        return self.tuner.data["Channel"]

    ## --------------------------------------------------------------
    ## Description : set the frequency
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-29-2021 17:29:13
    ## --------------------------------------------------------------
    def setFrequency(self, freq):
        self.tuner.setFrequency(freq)
        

if __name__ == '__main__':

    import sys
    sys.path

    import configparser
    config = configparser.ConfigParser()
    config.read("/home/pi/rpiCarGps/rpiCarGps.cfg")

    altFreq = []

    def printData(data):
        print('\033[2J')
        # print('\033[%sA'%(len(data)+2))
        print("=========================")
        print("Press key (u=search up, d=search down, s:f=set freq, q=quit): ")
        if ("altFreq1" in data and not data["altFreq1"] in altFreq): altFreq.append(data["altFreq1"])
        if ("altFreq2" in data and not data["altFreq2"] in altFreq): altFreq.append(data["altFreq2"])
        for d in data:
            if type(data[d]) is list:
                out = "".join(data[d]).strip()
            else:
                out = data[d]
            print("%s: %s"%(d,out))
        print("=========================")
        print("alt. freq. %s"%altFreq)

        config["Radio"]["lastfreq"] = "%s"%data["Channel"]


    signal("fromRadio").connect(printData)
    
    r = myRadio(config.getfloat("Radio","lastfreq"),0x10,1)
    r.start()

    altIndex = 0
    while 1:
        cmd = input("Press key (u=search up, d=search down, s:f=set freq, m=mute, p=play, , q=quit): ").lower()
        if "q" in cmd:
            r.Doit = False
            print("quitting")
            break
        elif "s" in cmd:
            f = float(cmd.split(":")[1])
            r.tuner.setFrequency(f)
            altFreq.clear()
        elif "u" in cmd:
            r.tuner.search(1)
            altFreq.clear()
        elif "d" in cmd:
            r.tuner.search(0)
            altFreq.clear()
        elif "a" in cmd:
            altIndex = (altIndex+1)%len(altFreq)
            r.tuner.setFrequency(altFreq[altIndex])
            print("alternative %s/%s"%(altIndex,len(altFreq)))
        elif "m" in cmd:
            r.tuner.Mute(1)
        elif "p" in cmd:
            r.tuner.Mute(0)
    
    time.sleep(2)
    with open("/home/pi/rpiCarGps/rpiCarGps.cfg", 'w') as configfile:
        config.write(configfile)                 
