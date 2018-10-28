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

class Rate(Counter):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        super(Rate, self).__init__(parent,w,h,name,title)

        #self.units = "m/s"
        self.units = "%"
        self.update("0")

    ## --------------------------------------------------------------
    ## Description : update altitude
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        self.Value.set_markup("<span font_desc=\"30\">%s</span>"%value)
        self.Units.set_markup("<span font_desc=\"20\">%s</span>"%self.units)
        return True
