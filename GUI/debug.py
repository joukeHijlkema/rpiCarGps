#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Debug
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. août 15:38 2017
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

print("GTK version {}.{}.{}".format(Gtk.get_major_version (),Gtk.get_minor_version (),Gtk.get_micro_version ()))

myCss = Gtk.CssProvider()
myCss.load_from_path("test.css")
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), 
    myCss,     
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)


builder = Gtk.Builder()
builder.add_from_file("debug.glade")

window  = builder.get_object("mainWindow")

window.show_all()
window.connect("delete-event",Gtk.main_quit)

Gtk.main()




      
