#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 21:51 2019
#   - Initial Version 1.0
#  =================================================
import time

from Classes.myTea5767 import myTea5767

class myRadio(object):
    """Documentation for myRadio

    """
    def __init__(self,i2c_address=0x60,i2c_bus=1):
        super(myRadio, self).__init__()
        self.tuner = myTea5767(i2c_address,i2c_bus)

        
    ## --------------------------------------------------------------
    ## Description : quit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 11-26-2019 13:26:39
    ## --------------------------------------------------------------
    def Quit (self):
        ##todo: mute device when quiting
        self.tuner.Quit()
        print("closed")


if __name__ == '__main__':

    r = myRadio()
    more = True
    while more:
        more = r.tuner.Search("up")
        time.sleep(3)
    r.Quit()
    time.sleep(1)
    
