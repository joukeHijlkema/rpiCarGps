#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. août 14:24 2017
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

import sys
sys.path.append("../GPS")
from GPS.gtkNavit import gtkNavit

import dbus
import configparser
from blinker import signal

config = configparser.ConfigParser()
config.read("/home/pi/rpiCarGps/rpiCarGps.cfg")

for i in eval(config.get("Items","Active")):
    exec("from .Parts.{item} import {item}".format(item=i))

class mainWindow(Gtk.Window):
    mode   = "Day"
    items  = {}
        
    def __init__(self):
        "docstring"
        super(mainWindow, self).__init__()
        print("gtk version = %s.%s.%s"%(Gtk.get_major_version(),Gtk.get_minor_version(),Gtk.get_micro_version()))

        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/pi/rpiCarGps/GUI/Gui.glade")
        
        handlers = {
            "onDeleteWindow"      : self.Quit,
            "onQuitButtonPressed" : self.Quit,
            "onToggleNightDay"    : self.toggleNightDay,
            "Action"              : self.Action
        }

        self.builder.connect_signals(handlers)

        W = config.getint("Items","Width")
        H = config.getint("Items","Height")
        W2 = config.getint("Items","GpsWidth")
        W1 = W-W2
        window   = self.builder.get_object("mainWindow")
        if config.getboolean("Items","Fullscreen"):
            window.fullscreen()
        else:
            window.set_default_size(W,H)
            window.set_size_request(W,H)
        navCont  = self.builder.get_object("navitContainer")
        myNavit  = gtkNavit(None,W2,H)
        navCont.add(myNavit)

        ## Counters
        butCont = self.builder.get_object("buttonContainer")
        
        for i in eval(config.get("Items","Active")):
            print("doing %s"%i)
            args=["w=%s"%W1]
            for kw in config.items(i):
                args.append("{key}={val}".format(key=kw[0],val=kw[1]))
            
            self.items[i]  = eval("{name}(self,{arguments})".format(
                name          = i,
                arguments     = ",".join(args)
            ))
            butCont.add(self.items[i])

        self.setStyle("/home/pi/rpiCarGps/GUI/Styles/%s/dayStyles.css"%config.get("Items","Config"))
        
        self.toRadio = signal("toRadio")
        self.fromRadio = signal("fromRadio")
        self.fromRadio.connect(self.gotRadioSignal)
        
        window.show_all()
        myNavit.start()

    ## --------------------------------------------------------------
    ## Description : treat signal received from radio
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 28-31-2019 11:31:54
    ## --------------------------------------------------------------
    def gotRadioSignal (self,data):
        print("GUI: received %s from Radio"%data)
        for i in data:
            print("%s: %s"%(i,data[i]))
        C = " : %s MHz"%data["Channel"] if "Channel" in data else ""
        S = "%s"%data["Station"] if "Station" in data else ""
        self.builder.get_object("radioInfo").set_text("%s%s"%(S,C))
        self.builder.get_object("signalStrength").set_value(float(data["Strength"]))

    ## --------------------------------------------------------------
    ## Description : GUI actions
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 26-06-2019 14:06:35
    ## --------------------------------------------------------------
    def Action (self,args):
        print(args.get_name())
        if "seekUp" in args.get_name():
            self.toRadio.send("seekUp")
        elif "seekDown" in args.get_name():
            self.toRadio.send("seekDown")

    ## --------------------------------------------------------------
    ## Description : set the style
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 22-52-2017 13:52:36
    ## --------------------------------------------------------------
    def setStyle (self,path):
        self.myCss = Gtk.CssProvider()
        self.myCss.load_from_path(path)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), 
            self.myCss,     
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    ## --------------------------------------------------------------
    ## Description : Quit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-26-2017 14:26:50
    ## --------------------------------------------------------------
    def Quit (self,who):
        Gtk.main_quit()

    ## --------------------------------------------------------------
    ## Description : toggle night and day mode
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-27-2017 14:27:11
    ## --------------------------------------------------------------
    def toggleNightDay (self,who):
        bus     = dbus.SessionBus()
        object  = bus.get_object("org.navit_project.navit","/org/navit_project/navit/default_navit")
        iface   = dbus.Interface(object,dbus_interface="org.navit_project.navit")
        iter    = iface.attr_iter()
        path    = object.get_attr_wi("navit",iter)
        navit   = bus.get_object('org.navit_project.navit', path[1])
        print(navit)
        iface.attr_iter_destroy(iter)
        
        if self.mode=="Day":
            print("switch to night")
            navit.set_layout("Car-dark")
            self.setStyle("GUI/Styles/%s/nightStyles.css"%config.get("Items","Config"))
            self.mode  = "Night"
        else:
            print("switch to day")
            navit.set_layout("Car")
            self.setStyle("GUI/Styles/%s/dayStyles.css"%config.get("Items","Config"))
            self.mode  = "Day"
