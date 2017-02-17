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

def testRun():
    for s in range(100):
        myDash.speedCounter.display(s)
        time.sleep(0.05)
        window.repaint()    

if __name__ == "__main__":

    Gps = myGps()
    
    app = QtWidgets.QApplication(sys.argv)
    myDash = Ui_Dashboard()
    window = QtWidgets.QMainWindow()
    myDash.setupUi(window)
    window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    window.showFullScreen()
    myDash.testButton.clicked.connect(testRun)

    
    sys.exit(app.exec_())

    
