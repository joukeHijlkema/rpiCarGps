#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 09:13 2017
#   - Initial Version 1.0
#  =================================================

from gi.repository import Gtk
import subprocess, os
import threading

class Navit(Gtk.Box,threading.Thread):
    def __init__(self,parent,w,h):
        "docstring"
        super(Gtk.Box, self).__init__()
        threading.Thread.__init__(self)
        
        self.socket = Gtk.Socket.new()
        self.socket.set_size_request(w, h)
        self.socket.show()
        self.add(self.socket)

        
    ## --------------------------------------------------------------
    ## Description : run
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-59-2017 10:59:06
    ## --------------------------------------------------------------
    def run (self):
        id = Gtk.Socket.get_id(self.socket)
        print("socket id = 0x%x"%Gtk.Socket.get_id(self.socket))
        subprocess.Popen("navit", env=dict(os.environ, NAVIT_XID="%s"%id))
        
    
