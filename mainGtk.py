#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:47 2017
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk

from GPS.gtkNavit import Navit
from GTK.speedMeter import speedMeter
from GTK.dayDist import dayDist
from GTK.totDist import totDist

win = Gtk.Window()
win.set_size_request(1024, 600)
win.connect("delete-event", Gtk.main_quit)

grid = Gtk.Grid()
grid.show()
win.add(grid)

mySpeedMeter  = speedMeter(win,320,20,"speedMeter","Vitesse:")
myDayDist     = dayDist(win,320,20,"dayDist","Aujourd'hui:")
myTotDist     = totDist(win,320,20,"totDist","Totale:")
myNavit       = Navit(win,700,600)

myTotDist.set_vexpand(True)
myTotDist.set_valign(Gtk.Align.START)

grid.attach(mySpeedMeter,0,0,1,1)
grid.attach(myDayDist,0,1,1,1)
grid.attach(myTotDist,0,2,1,1)
grid.attach(myNavit,1,0,1,4)

myNavit.run()

myCss = Gtk.CssProvider()
print("loading css : %s"%Gtk.CssProvider.load_from_path(myCss,"/home/hylkema/Projects/rpiCarGps/GTK/Styles.css"))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), 
    myCss,     
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

win.show_all()
Gtk.main()
