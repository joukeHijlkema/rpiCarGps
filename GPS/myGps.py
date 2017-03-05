#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# myGps
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - Sun Feb 12 17:57:16 2017
#   - Initial Version 1.0
#  =================================================
import gps
from PyQt5 import QtCore, QtGui
import time
import random

class myGps(QtCore.QThread):
    
    newData = QtCore.pyqtSignal(object)
    test    = False
    data    = {}
    def __init__(self):
        "listen to gps data and emit some if anything new arrives"
        QtCore.QThread.__init__(self)
        
        # Listen on port 2947 (gpsd) of localhost
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    ## --------------------------------------------------------------
    ## Description :run
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 17-52-2017 18:52:05
    ## --------------------------------------------------------------
    def run (self):
        if self.test==True:
            while True:
                self.data.clear()
                self.data['speed']=random.randrange(0,100,1)
                self.newData.emit(self.data)
                time.sleep(1)
        else:
            while True:
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
                        self.newData.emit(self.data)
                except KeyError:
                    pass
                except KeyboardInterrupt:
                    quit()
                except StopIteration:
                    self.session = None
                    print("GPSD has terminated")
