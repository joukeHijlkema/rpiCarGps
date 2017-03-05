#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. mars 13:53 2017
#   - Initial Version 1.0
#  =================================================

import os
import glob
import time
from PyQt5 import QtCore, QtGui

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

class myTemp(QtCore.QThread):

    newData       = QtCore.pyqtSignal(object)
    base_dir      = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file   = device_folder + '/w1_slave'

    def __init__(self):
        "read temperature from probe"
        QtCore.QThread.__init__(self)

    ## --------------------------------------------------------------
    ## Description :run
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 04-02-2017 14:02:21
    ## --------------------------------------------------------------
    def run (self):
        while True:
	    self.newData.emit(self.readTemp())
	    time.sleep(5)

    ## --------------------------------------------------------------
    ## Description :read raw temp
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 04-04-2017 14:04:10
    ## --------------------------------------------------------------
    def readRaw (self):
        lines=["blabla"]
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            f     = open(self.device_file, 'r')
            lines = f.readlines()
            f.close()
        return lines

    ## --------------------------------------------------------------
    ## Description :read temp
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 04-04-2017 14:04:44
    ## --------------------------------------------------------------
    def readTemp (self):
        lines = self.readRaw()
        equals_pos = lines[1].find('t=')
        temp_c="-1000"
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0

        print "temp = %s °C"%temp_c
        return temp_c
