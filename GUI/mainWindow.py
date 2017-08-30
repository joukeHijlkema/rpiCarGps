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
# gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

import sys
sys.path.append("../GPS")
from GPS.gtkNavit import gtkNavit

import dbus
import configparser

config = configparser.ConfigParser()
config.read("rpiCarGps.cfg")

for i in eval(config.get("Items","Active")):
    exec("from .Parts.{item} import {item}".format(item=i))

class mainWindow(Gtk.Window):
    mode   = "Day"
    items  = {}
        
    def __init__(self):
        "docstring"
        super(mainWindow, self).__init__()
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("GUI/Gui.glade")
        
        handlers = {
            "onDeleteWindow": self.Quit,
            "onQuitButtonPressed": self.Quit,
            "onToggleNightDay": self.toggleNightDay
        }

        self.builder.connect_signals(handlers)

        window   = self.builder.get_object("mainWindow")
        navCont  = self.builder.get_object("navitContainer")
        myNavit  = gtkNavit(None,config.getint("Items","Width"),config.getint("Items","Height"))
        navCont.add(myNavit)

        ## Counters
        butCont          = self.builder.get_object("buttonContainer")
        
        for i in eval(config.get("Items","Active")):
            print("doing %s"%i)
            args=[]
            for kw in config.items(i):
                args.append("{key}={val}".format(key=kw[0],val=kw[1]))
            
            self.items[i]  = eval("{name}(self,{arguments})".format(
                name          = i,
                arguments     = ",".join(args)
            ))
            butCont.add(self.items[i])

        self.setStyle("GUI/Styles/dayStyles.css")
        
        window.show_all()
        myNavit.start()

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
        object  = bus.get_object("org.navit_project.navit","/org/navit_project/navit")
        iface   = dbus.Interface(object,dbus_interface="org.navit_project.navit")
        iter    = iface.attr_iter()
        path    = object.get_attr_wi("navit",iter)
        navit   = bus.get_object('org.navit_project.navit', path[1])
        print(navit)
        iface.attr_iter_destroy(iter)
        
        if self.mode=="Day":
            print("switch to night")
            navit.set_layout("Car-dark")
            self.setStyle("GUI/Styles/nightStyles.css")
            self.mode  = "Night"
        else:
            print("switch to day")
            navit.set_layout("Car")
            self.setStyle("GUI/Styles/dayStyles.css")
            self.mode  = "Day"
