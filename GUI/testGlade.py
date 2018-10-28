#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. août 11:25 2017
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

# import sys
# sys.path.append("../../GPS")
# from gtkNavit import gtkNavit


# def Quit(who):
#     Gtk.main_quit()

# def toggleNightDay:
    

# builder = Gtk.Builder()
# builder.add_from_file("Gui.glade")

# handlers = {
#     "onDeleteWindow": Quit,
#     "onQuitButtonPressed": Quit
#     "onToggleNightDay": toggleNightDay
# }

# builder.connect_signals(handlers)

# window   = builder.get_object("mainWindow")
# grid     = builder.get_object("grid")
# myNavit  = gtkNavit(None,700,600)
# grid.attach(myNavit,1,0,1,8)

# window.show_all()
# myNavit.start()

from mainWindow import mainWindow

myWindow = mainWindow()

Gtk.main()

