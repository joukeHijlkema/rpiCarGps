#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. avril 16:24 2017
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from GTK.mainGtk import mainGtk as MainWindow
from GPS.myGps import Gps

win = MainWindow(1024,600)
def Quit(arg1,arg2):
    print arg1
    print arg2
    myGps.Doit=False
    Gtk.main_quit()

# GPS
myGps = Gps()
myGps.start()

win.connect("delete-event",Quit)

Gtk.main()

