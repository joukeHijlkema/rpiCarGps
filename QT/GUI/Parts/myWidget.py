#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 15:52 2017
#   - Initial Version 1.0
#  =================================================
from PyQt5 import QtCore, QtGui, QtWidgets

class myWidget(QtWidgets.QWidget):
    def __init__(self,parent):
        QtWidgets.QWidget.__init__(self)

        self.Hfont = QtGui.QFont()
        self.Hfont.setPointSize(50)
        
        self.Bfont = QtGui.QFont()
        self.Bfont.setPointSize(30)
        
        self.Mfont = QtGui.QFont()
        self.Mfont.setPointSize(20)
        
        self.Sfont = QtGui.QFont()
        self.Sfont.setPointSize(15)
        
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.setSpacing(0)

