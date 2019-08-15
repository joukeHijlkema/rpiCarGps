#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. août 13:25 2019
#   - Initial Version 1.0
#  =================================================
import time

from Classes.myI2C import myI2C

class myTea5767(object):
    """Documentation for myTea5767

    """
    def __init__(self,i2c_address,i2c_bus):
        super(myTea5767, self).__init__()

        print("initilizing hardware")
        self.outFormat = {
            "mute"                   :[(0,7)],
            "search"                 :[(0,6)],
            "freq"                   :[(0,5),(1,0)],              
            "search up"              :[(2,7)],
            "SSL"                    :[(2,6),(2,5)],
            "HLSI"                   :[(2,4)],
            "force mono"             :[(2,3)],
            "mute right"             :[(2,2)],
            "mute left"              :[(2,1)],
            "SWP1"                   :[(2,0)],
            "SWP2"                   :[(3,7)],
            "stand-by"               :[(3,6)],
            "japanese band limits"   :[(3,5)],
            "XTAL"                   :[(3,4)],
            "soft mute"              :[(3,3)],
            "high cut control"       :[(3,2)],
            "stereo noise canceling" :[(3,1)],
            "SI"                     :[(3,0)],
            "PLLREF"                 :[(4,7)],
            "DTC"                    :[(4,6)]
            }
        self.inFormat = {
            "ready"      :[(0,7)],
            "band limit" :[(0,6)],
            "freq"       :[(0,5),(1,0)],
            "stereo"     :[(2,7)],
            "IF"         :[(2,6),(2,0)],
            "adc ouput"  :[(3,7),(3,4)],
            "Chip id"    :[(3,5),(3,1)],
            "Dummy"      :[(3,0),(4,0)]
        }

        self.i2c = myI2C(i2c_address,i2c_bus,self.inFormat,self.outFormat)
        self.i2c.Set("mute",1)
        self.i2c.Set("freq",self.calcFreq(87.5))
        self.i2c.Set("SSL",3)
        self.i2c.Set("XTAL",1)
        self.i2c.Set("HLSI",1)
        self.i2c.Set("high cut control",1)
        self.i2c.Set("stereo noise canceling",1)

        self.i2c.Send()
        self.i2c.Read()
        print("done")

    ## --------------------------------------------------------------
    ## Description : set the frequency
    ## NOTE : this fills databits 0 and 1
    ## -
    ## Author : jouke hylkema
    ## date   : 11-53-2019 14:53:12
    ## --------------------------------------------------------------
    def calcFreq (self,freq):
        
        if(freq<87.5):
            freq=108
        elif(freq>107.9):
            freq=87.5
        return int (4 * (freq * 1000000 + 225000) / 32768) 
        
    ## --------------------------------------------------------------
    ## Description : quit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 11-26-2019 13:26:39
    ## --------------------------------------------------------------
    def Quit (self):
        self.i2c.Set("mute",1)
        self.i2c.Send()
        print("closed")

    ## --------------------------------------------------------------
    ## Description : Search
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-36-2019 15:36:58
    ## --------------------------------------------------------------
    def Search (self,dir):
        # start search
        f = self.i2c.getByName("In","freq")
        print(f)
        if dir=="up":
            self.i2c.Set("search up",1)
            self.i2c.Set("freq",f+1)
        else:
            self.Set("search up",0)
            self.i2c.Set("freq",f-1)
        
        self.i2c.Set("mute",1)
        self.i2c.Set("search",1)
        self.i2c.Send()
        time.sleep(0.03)
        self.i2c.Read()
        while not self.i2c.getByName("In","ready"):
            time.sleep(0.03)
            self.i2c.Read()
            if self.i2c.getByName("In","band limit"):
                print("out of range")
                return False

        self.i2c.Set("mute",0)
        self.i2c.Set("search",0)
        self.i2c.Send()
        self.i2c.Info("READ")
        return True
 
