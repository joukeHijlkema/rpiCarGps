#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:53 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from Counter import Counter

class dayDist(Counter):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        super(dayDist, self).__init__(parent,w,h,name,title)

        self.units = "km"
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
        # print "update dayDist to %s (%s)"%(v,value)
        self.Value.set_markup("<span font_desc=\"30\">%3.1f</span>"%v)
        self.Units.set_label("%s"%self.units)
        return True
