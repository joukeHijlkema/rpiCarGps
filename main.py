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
from dashboard import Ui_Dashboard
import time

from GPS import myGps

class mainWindow(Ui_Dashboard):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        # self.window.showFullScreen()
        self.testButton.clicked.connect(self.testRun)

        self.Gps = myGps.myGps()
        self.threads.append(Gps)
            
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

    
