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
from blinker import signal

from GPS.gtkNavit import Navit
from speedMeter import speedMeter
from dayDist import dayDist
from totDist import totDist

class mainGtk(Gtk.Window):
    def __init__(self,w,h):
        "docstring"
        super(mainGtk, self).__init__(title="Car GPS")
        print "main window"
        self.set_size_request(w, h)

        grid = Gtk.Grid()
        grid.show()
        self.add(grid)

        self.mySpeedMeter  = speedMeter(self,320,20,"speedMeter","Vitesse:")
        self.myDayDist     = dayDist(self,320,20,"dayDist","Aujourd'hui:")
        self.myTotDist     = totDist(self,320,20,"totDist","Totale:")
        self.myNavit       = Navit(self,700,600)

        self.myTotDist.set_vexpand(True)
        self.myTotDist.set_valign(Gtk.Align.START)

        grid.attach(self.mySpeedMeter,0,0,1,1)
        grid.attach(self.myDayDist,0,1,1,1)
        grid.attach(self.myTotDist,0,2,1,1)
        grid.attach(self.myNavit,1,0,1,4)

        self.myNavit.run()

        # Stylesheets
        myCss = Gtk.CssProvider()
        print("loading css : %s"%Gtk.CssProvider.load_from_path(myCss,"/home/hylkema/Projects/rpiCarGps/GTK/Styles.css"))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), 
            myCss,     
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        #Signaling
        gpsData = signal('Gps')
        gpsData.connect(self.gotGpsData)

        self.show_all()


    ## --------------------------------------------------------------
    ## Description : signaling
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 21-23-2017 17:23:21
    ## --------------------------------------------------------------
    def gotGpsData(self,sender, **kw):
        print("Got a signal sent by %r, data= %r" %(sender,kw))
        self.mySpeedMeter.update(kw['data']['speed'])
        
       

        



