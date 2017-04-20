#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 15:25 2017
#   - Initial Version 1.0
#  =================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from myWidget import myWidget

class speedMeter(myWidget):
    def __init__(self,parent):
        "speed meter widget"
        myWidget.__init__(self,parent)
        
        self.speed = QtWidgets.QLabel()
        self.units = QtWidgets.QLabel()

        self.speed.setText("110")
        self.speed.setFont(self.Hfont)
        self.speed.setMinimumSize(QtCore.QSize(150, 0))
        self.speed.setStyleSheet("color: blue;")
        self.units.setText("km/h")
        self.units.setFont(self.Sfont)
        
        self.hbox.addWidget(self.speed)
        self.hbox.addWidget(self.units)
        self.hbox.setObjectName("speedMeter")

    ## --------------------------------------------------------------
    ## Description :update
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 26-11-2017 18:11:33
    ## --------------------------------------------------------------
    def update (self,value):
        self.speed.setText("%i"%value)
