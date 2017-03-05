#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# main
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - Fri Feb  3 19:19:04 2017
#   - Initial Version 1.0
#  =================================================

import sys
from PyQt5 import QtWidgets,QtCore
from GUI.dashboard import Ui_Dashboard
import time

from GPS import myGps
from TEMP import myTemp

class mainWindow(Ui_Dashboard):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.window.showFullScreen()
        self.testButton.clicked.connect(self.testRun)

        self.Gps = myGps.myGps()
        self.Gps.newData.connect(self.onGpsDataReady)
        self.Gps.start()

        self.Temp = myTemp.myTemp()
        self.Temp.newData.connect(self.onTempDataReady)
        self.Temp.start()

    ## --------------------------------------------------------------
    ## Description :called when gpsdata is ready
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 18-19-2017 15:19:53
    ## --------------------------------------------------------------
    def onGpsDataReady (self,data):
        print(data)
        self.speedCounter.display(data['speed'])
        
            
    ## --------------------------------------------------------------
    ## Description :called when tempdata is ready
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 18-19-2017 15:19:53
    ## --------------------------------------------------------------
    def onTempDataReady (self,data):
        print(data)
        self.tempValue.display("%2.1f"%data)
        
            
    ## --------------------------------------------------------------
    ## Description :test run
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 17-03-2017 19:03:06
    ## --------------------------------------------------------------
    def testRun (self):
        for s in range(100):
            self.speedCounter.display(s)
            time.sleep(0.05)
            self.window.repaint()    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.window.show()
    sys.exit(app.exec_())

    
