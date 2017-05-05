#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - lun. mai 22:33 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from Counter import Counter
import arrow

class Time(Counter):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        super(Time, self).__init__(parent,w,h,name,title)

        self.units = "°C"
        self.update("0")

    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        v = value.split("#")
        t = arrow.get(v[0]).to('Europe/Paris')
        if len(v)>1:
            temp = float(v[1])
        else:
            temp = 0.0
        self.Value.set_markup("<span font_desc=\"30\">%s - %3.1f</span>"%(t.format('HH:mm:ss'),temp))
        self.Units.set_markup("<span font_desc=\"20\">%s</span>"%self.units)
        return True
