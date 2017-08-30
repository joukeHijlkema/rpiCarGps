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
from .Counter import Counter
import arrow

class Time(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(Time, self).__init__(parent,*args,**kw)

        self.units = "°C"
        self.update("2009-12-31 20:59:59#99")

    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        print("in time %s"%value)
        v = value.split("#")
        print(v[0])
        t = arrow.get(v[0]).to('Europe/Paris')
        print(t)
        if len(v)>1:
            data = "{:<s} - {:>3.1f}".format(t.format('ddd D/M HH:mm'),float(v[1]))
        else:
            data = "{:<s}".format(t.format('ddd D/M HH:mm'))
            self.units = ""
        self.Value.set_label(":<s"%data)
        self.Units.set_label("%s"%self.units)
        return True
