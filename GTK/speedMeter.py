#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:53 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk, Gdk
from Counter import Counter

class speedMeter(Counter):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        print("speedMeter")
        super(speedMeter, self).__init__(parent,w,h,name,title)

        self.units = "km/h"
        self.update(0)

    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        
        v = self.conversion[self.units]*value

        self.Value.set_markup("<span foreground=\"red\" font_desc=\"60\">%4.1f</span>"%v)
        self.Units.set_label("%s"%self.units)
        
        return True
