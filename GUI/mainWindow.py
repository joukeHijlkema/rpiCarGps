#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 15:35 2017
#   - Initial Version 1.0
#  =================================================
from PyQt5 import QtCore, QtGui, QtWidgets

from Parts.speedMeter import speedMeter
from Parts.Counter import Counter

import arrow
from DB import dataBase

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)

        self.setObjectName("myCarGps")
        self.showFullScreen()
        
        self.cw =  QtWidgets.QWidget(self)
        self.cw.setObjectName("centralwidget")
        self.setCentralWidget(self.cw)

        self.leftWidget = QtWidgets.QWidget(self.cw)
        self.leftWidget.setGeometry(QtCore.QRect(0, 0, 275, 561))
        self.left       = QtWidgets.QVBoxLayout(self.leftWidget)
        
        self.speed  = speedMeter(self.cw)
        self.dstDay = Counter(self.cw,"distance today:","Km")
        self.dstTtl = Counter(self.cw,"distance total:","Km")
        self.temp   = Counter(self.cw,"Temperature:","°C")

        # Quit button
        self.quitButton = QtWidgets.QPushButton(self.cw)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.setText("quit")

        # Time and date
        self.timeField = QtWidgets.QLabel(self.cw)
        self.timeField.setText("time and date")
        self.timeField.setFont(self.speed.Mfont)
        
        self.left.addLayout(self.speed.hbox)
        self.left.addLayout(self.dstDay.hbox)
        self.left.addLayout(self.dstTtl.hbox)
        self.left.addLayout(self.temp.hbox)

        self.left.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.left.addWidget(self.timeField)
        self.left.addWidget(self.quitButton)

        self.quitButton.clicked.connect(self.close)

        self.db = dataBase.dataBase("Jouke","!Jouke","localhost","busGps")

    ## --------------------------------------------------------------
    ## Description :called when gpsdata is ready
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 18-19-2017 15:19:53
    ## --------------------------------------------------------------
    def onGpsDataReady (self,data):
        print(data)
        self.speed.update(data['speed'])
        self.actualTime = arrow.get(data['time'])
        self.timeField.setText(self.actualTime.to('local').format("ddd MMM YYYY HH:mm"))
        self.db.Put(("INSERT INTO Gps (Lat,Lon,Time) VALUES (%s,%s,%s)"),
                    (data['lat'],data['lon'],data['time']))
