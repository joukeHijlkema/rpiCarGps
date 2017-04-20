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

class Counter(Gtk.Box):
    def __init__(self,parent,w,h,name,title):
        "docstring"
        print("Counter")
        super(Counter, self).__init__()

        self.set_name(name)
        self.set_spacing(10)
        
        self.Title  = Gtk.Label.new(title)
        self.Title.set_name("Title")
        self.Title.set_size_request(0.3*w,h)
        self.Title.set_xalign(0)
        
        self.Value  = Gtk.Label.new("---")
        self.Value.set_name("Value")
        self.Value.set_size_request(0.5*w,h)
        self.Value.set_xalign(1)
        
        self.Units  = Gtk.Label.new("--")
        self.Units.set_name("Units")
        self.Units.set_size_request(0.1*w,h)
        self.Units.set_xalign(0)

        self.add(self.Title)
        self.add(self.Value)
        self.add(self.Units)
        
        self.set_size_request(w,h)

    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        v=0.0
        if self.units=="km":
            v = 0.001*value

        self.Value.set_text("%d"%v)
        self.Units.set_text("%s"%self.units)
