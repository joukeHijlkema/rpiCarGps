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
from .Counter import Counter
from blinker import signal

class dayDist(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(dayDist, self).__init__(parent,*args,**kw)

        self.Value.set_width_chars(3)
        self.Value.set_max_width_chars(3)

        self.units = "km"
        self.update(0)
        

        self.back = Gtk.Button.new_with_label("-")
        self.back.set_hexpand(True)
        self.back.set_size_request(25,10)
        self.add(self.back)

        self.reset = Gtk.Button.new_with_label("0")
        self.reset.set_hexpand(True)
        self.add(self.reset)

        self.offset = 0
        self.back.connect("clicked",self.changeOffset,1)
        self.reset.connect("clicked",self.changeOffset,0)
        self.backSignal  = signal('dayTot')

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
            self.back.set_label("-%s"%self.offset)
        else:
            self.offset=0
            self.color = "blue"
            self.back.set_label("-")
        self.backSignal.send(self.offset)
