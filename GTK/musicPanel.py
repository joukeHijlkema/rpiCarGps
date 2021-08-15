#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. août 11:13 2021
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from blinker import signal

class musicPanel(Gtk.Box):
    """Documentation for musicPanel

    """
    def __init__(self,parent,w,h,name):
        super(musicPanel, self).__init__()
        self.parent = parent
        self.w      = w
        self.h      = h
        self.name   = name

        self.set_name(name)
        self.play = Gtk.Button.new_from_stock("gtk-media-play")

        self.add(self.play)
        
    
