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

class tripDist(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(tripDist, self).__init__(parent,*args,**kw)
        self.parent = parent

        self.units = "km"
        self.update(0)
        self.Value.set_width_chars(4)
        self.Value.set_max_width_chars(4)

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
        dialog = Gtk.MessageDialog(self.parent, 0, Gtk.MessageType.WARNING,
                                   Gtk.ButtonsType.OK_CANCEL, "Reset trip ?")
        rep = dialog.run()
        if rep == Gtk.ResponseType.OK:
            self.returnSignal.send("reset")
        dialog.destroy()
