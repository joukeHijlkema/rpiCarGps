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

    conversion={"km":0.001,"km/h":3.6,"m/s":1.0,"m":1.0,"%":100.0}
    
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(Counter, self).__init__()
        # print(kw)

        self.set_valign(Gtk.Align.START)

        name = kw["name"] if "name" in kw else "noName"
        self.set_name(name)
        
        if "floatdown" in kw:
            print("float down")
            self.set_vexpand(True)

        w = kw["w"] if "w" in kw else 324
        h = kw["h"] if "h" in kw else 10

        if "title" in kw:
            title = kw["title"]
            self.Title  = Gtk.Label.new(title)
            self.Title.set_name("Title")
            # self.Title.set_halign(Gtk.Align.START)
            self.Title.set_alignment(0.0,0.5)
            self.add(self.Title)
            self.Title.set_width_chars(8)
            self.Title.set_max_width_chars(8)

        
        self.Value  = Gtk.Label.new("---")
        self.Value.set_name("Value")
        self.Value.set_alignment(0.0,0.5)
        
        self.Units  = Gtk.Label.new("--")
        self.Units.set_name("Units")
        self.Units.set_alignment(0.0,0.5)

        self.add(self.Value)
        self.add(self.Units)

        self.set_size_request(w,h)

        self.updateSignal = signal(name)
        self.returnSignal = signal("%s_return"%name)
        self.updateSignal.connect(self.update)

        self.form = kw["format"] if "format" in kw else "{:<3d}"

    ## --------------------------------------------------------------
    ## Description : update the value
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        
        if "d" in self.form:
            v = int(self.conversion[self.units]*value)
        elif "f" in self.form:
            v = float(self.conversion[self.units]*value)
            
        self.Value.set_label(self.form.format(v))
        self.Units.set_label("%s"%self.units)

        return True        
