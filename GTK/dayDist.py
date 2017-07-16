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

        self.back = Gtk.Button.new_with_label("-")
        self.back.set_hexpand(True)
        self.add(self.back)

        self.reset = Gtk.Button.new_with_label("0")
        self.reset.set_hexpand(True)
        self.add(self.reset)

        self.offset = 0
        self.back.connect("clicked",self.changeOffset,1)
        self.reset.connect("clicked",self.changeOffset,0)

    ## --------------------------------------------------------------
    ## Description : chage the offset value
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 16-15-2017 12:15:52
    ## --------------------------------------------------------------
    def changeOffset (self,widget,delta):
        if delta==1:
            self.offset+=1
            self.color = "red"
        else:
            self.offset=0
            self.color = "blue"
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
        self.Value.set_markup("<span foreground=\"%s\" font_desc=\"30\">%3.1f</span>"%(self.color,v))
        self.Units.set_label("%s"%self.units)
        return True
