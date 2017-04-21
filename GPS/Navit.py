#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - lun. avril 13:45 2017
#   - Initial Version 1.0
#  =================================================

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import time


class Navit(QtWidgets.QWidget):
    def __init__(self,parent):
        "docstring"
        QtWidgets.QWidget.__init__(self,parent)
        self.process = QtCore.QProcess(self)
        # process.startDetached( "navit" )
        self.process.start( "navit" )

        # wait for Navit
        time.sleep(2)

        proc = subprocess.Popen("xwininfo -int -name Navit", stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        for l in out.split("\n"):
            if "Window id" in l:
                Id = int(l.split(":")[2].split()[0])
                QW = QtGui.QWindow.fromWinId(Id)
                QW.setFlags(QtCore.Qt.FramelessWindowHint);
                Qwid = QtWidgets.QWidget.createWindowContainer(QW)
                layout = QtWidgets.QVBoxLayout(self);
                layout.addWidget(Qwid);
                self.setLayout(layout);
                

    ## --------------------------------------------------------------
    ## Description : quit navit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 19-38-2017 21:38:26
    ## --------------------------------------------------------------
    def Quit (self):
        self.process.terminate()
