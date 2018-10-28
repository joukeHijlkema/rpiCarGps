#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:47 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk,Gdk

from GPS.gtkNavit import gtkNavit
from speedMeter import speedMeter
from dayDist import dayDist
from tripDist import tripDist
from totDist import totDist
from Altitude import Altitude
from Rate import Rate
from Time import Time

class mainGtk(Gtk.Window):
    Init = True
    def __init__(self,w,h,path,real):
        "docstring"
        super(mainGtk, self).__init__(title="Car GPS")
        print "main window"
        self.set_size_request(w, h)
        if real:
            self.fullscreen()

        grid = Gtk.Grid()
        grid.show()
        self.add(grid)

        self.mySpeedMeter  = speedMeter(self,320,100,"speedMeter","")
        self.myDayDist     = dayDist(self,320,20,"dayDist","Jour:")
        self.mytripDist    = tripDist(self,320,20,"tripDist","Trip:")
        self.myTotDist     = totDist(self,320,20,"totDist","Total:")
        self.myAlt         = Altitude(self,320,20,"alt","Alt:")
        self.myRate        = Rate(self,320,20,"rate","Rate:")
        self.myTime        = Time(self,320,20,"Time","")
        self.myNavit       = gtkNavit(self,700,600)
        self.quitButton    = Gtk.Button.new_with_label("quit")

        self.myTotDist.set_vexpand(True)
        self.myTotDist.set_valign(Gtk.Align.START)

        self.quitButton.set_size_request(320,100);

        grid.attach(self.mySpeedMeter,0,0,1,1)
        grid.attach(self.myDayDist,0,1,1,1)
        grid.attach(self.mytripDist,0,2,1,1)
        grid.attach(self.myTotDist,0,3,1,1)
        grid.attach(self.myAlt,0,4,1,1)
        grid.attach(self.myRate,0,5,1,1)
        grid.attach(self.myTime,0,6,1,1)
        grid.attach(self.quitButton,0,7,1,1)
        grid.attach(self.myNavit,1,0,1,8)

        self.myNavit.start()

        # Stylesheets
        myCss = Gtk.CssProvider()
        myCss.load_from_path(path)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), 
            myCss,     
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.show_all()

        



