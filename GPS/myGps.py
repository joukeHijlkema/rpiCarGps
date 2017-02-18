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

class myGps(QtCore.QThread):
    netwData = QtCore.pyqtSignal(object)

    def __init__(self):
        "listen to gps data and emit some if anything new arrives"
        
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
        while True:
            print "running ..."
            try:
                report = self.session.next()
                # Wait for a 'TPV' report and display the current time
                # To see all report data, uncomment the line below
                # print(report)
                if report['class'] == 'TPV':
                    if hasattr(report, 'time'):
                        print(report.time)
                    if hasattr(report, 'speed'):
                        print(report.speed * gps.MPS_TO_KPH)
            except KeyError:
                pass
            except KeyboardInterrupt:
                quit()
            except StopIteration:
                session = None
                print("GPSD has terminated")
