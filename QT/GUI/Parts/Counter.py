#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 16:21 2017
#   - Initial Version 1.0
#  =================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from myWidget import myWidget

class Counter(myWidget):
    def __init__(self,parent,title,units):
        "Counter widget"
        myWidget.__init__(self,parent)

        self.title = QtWidgets.QLabel()
        self.dist  = QtWidgets.QLabel()
        self.units = QtWidgets.QLabel()

        self.title.setText(title)
        self.title.setFont(self.Sfont)
        self.title.setMinimumSize(QtCore.QSize(135, 0))
        
        self.dist.setText("0000")
        self.dist.setFont(self.Bfont)
        self.dist.setMinimumSize(QtCore.QSize(50, 0))
        self.dist.setStyleSheet("color: blue;")
        
        self.units.setText(units)
        self.units.setFont(self.Sfont)
        
        self.hbox.addWidget(self.title)
        self.hbox.addWidget(self.dist)
        self.hbox.addWidget(self.units)
