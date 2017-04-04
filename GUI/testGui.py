#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 15:39 2017
#   - Initial Version 1.0
#  =================================================
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from mainWindow import mainWindow

app = QtWidgets.QApplication(sys.argv)
window = mainWindow()
window.show()
sys.exit(app.exec_())
