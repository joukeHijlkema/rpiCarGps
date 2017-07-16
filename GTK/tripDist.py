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

class tripDist(Counter):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        super(tripDist, self).__init__(parent,w,h,name,title)

        self.units = "km"
        self.update(0)

        self.reset = Gtk.Button.new_with_label("0")
        self.reset.set_hexpand(True)
        self.add(self.reset)

        self.reset.connect("clicked",self.myReset)

    ## --------------------------------------------------------------
    ## Description : chage the offset value
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 16-15-2017 12:15:52
    ## --------------------------------------------------------------
    def myReset (self,widget):
        self.returnSignal.send("reset")
        print "reset trip"
    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        v = self.conversion[self.units]*value
        # print "update tripDist to %s (%s)"%(v,value)
        self.Value.set_markup("<span foreground=\"%s\" font_desc=\"30\">%d</span>"%(self.color,v))
        self.Units.set_label("%s"%self.units)
        return True
