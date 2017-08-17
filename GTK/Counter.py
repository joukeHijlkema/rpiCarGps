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
from blinker import signal

class Counter(Gtk.Box):

    conversion={"km":0.001,"km/h":3.6}
    
    def __init__(self,parent,w,h,name,title):
        "docstring"
        print("Counter")
        super(Counter, self).__init__()

        self.set_name(name)
        # self.set_spacing(10)

        if not title == "":
            w1=0.2*w
            w2=0.38*w
            w3=0.1*w
            self.Title  = Gtk.Label.new(title)
            self.Title.set_name("Title")
            self.Title.set_size_request(w1,h)
            self.add(self.Title)
        else:
            w2=0.8*w
            w3=0.1*w
        
        self.Value  = Gtk.Label.new("---")
        self.Value.set_name("Value")
        self.Value.set_size_request(w2,h)
        
        self.Units  = Gtk.Label.new("--")
        self.Units.set_name("Units")
        self.Units.set_size_request(w3,h)

        self.add(self.Value)
        self.add(self.Units)
        
        self.set_size_request(w,h)

        self.updateSignal = signal(name)
        self.returnSignal = signal("%s_return"%name)
        self.updateSignal.connect(self.update)

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
        # print "update Counter to %s (%s)"%(v,value)

        self.Value.set_markup("<span font_desc=\"30\">%d</span>"%v)
        self.Units.set_label("%s"%self.units)

        return True        
