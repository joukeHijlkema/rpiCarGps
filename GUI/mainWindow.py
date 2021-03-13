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
from gi.repository import Gtk, GObject, Gdk, GdkPixbuf, Gio, GLib

import sys
sys.path.append("../GPS")
from GPS.gtkNavit import gtkNavit

import dbus
import configparser
from blinker import signal

import svgutils.transform as sg
from lxml import etree

tmp_config = configparser.ConfigParser()
tmp_config.read("/home/pi/rpiCarGps/rpiCarGps.cfg")

for i in eval(tmp_config.get("Items","Active")):
    exec("from .Parts.{item} import {item}".format(item=i))

class mainWindow(Gtk.Window):
    mode   = "Day"
    items  = {}
        
    def __init__(self,config):
        "docstring"
        super(mainWindow, self).__init__()
        print("gtk version = %s.%s.%s"%(Gtk.get_major_version(),Gtk.get_minor_version(),Gtk.get_micro_version()))

        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/pi/rpiCarGps/GUI/Gui.glade")
        
        handlers = {
            "onDeleteWindow"      : self.Quit,
            "onQuitButtonPressed" : self.Quit,
            "onToggleNightDay"    : self.toggleNightDay,
            "Action"              : self.Action,
            "focusTab"            : self.focusTab,
            "levelReset"          : self.levelReset,
            "levelZoom"           : self.levelZoom
        }

        self.builder.connect_signals(handlers)
        self.config = config
        W = self.config.getint("Items","Width")
        H = self.config.getint("Items","Height")
        W2 = self.config.getint("Items","GpsWidth")
        W1 = W-W2
        window   = self.builder.get_object("mainWindow")
        if self.config.getboolean("Items","Fullscreen"):
            window.fullscreen()
        else:
            window.set_default_size(W,H)
            window.set_size_request(W,H)
        navCont  = self.builder.get_object("navitContainer")
        myNavit  = gtkNavit(None,W2,H-50)
        navCont.add(myNavit)

        ## Counters
        butCont = self.builder.get_object("buttonContainer")
        
        for i in eval(self.config.get("Items","Active")):
            print("doing %s"%i)
            args=["w=%s"%W1]
            for kw in self.config.items(i):
                args.append("{key}={val}".format(key=kw[0],val=kw[1]))
            
            self.items[i]  = eval("{name}(self,{arguments})".format(
                name          = i,
                arguments     = ",".join(args)
            ))
            butCont.add(self.items[i])

        self.setStyle("/home/pi/rpiCarGps/GUI/Styles/%s/dayStyles.css"%self.config.get("Items","Config"))
        
        self.toRadio = signal("toRadio")
        self.fromRadio = signal("fromRadio")
        self.fromRadio.connect(self.gotRadioSignal)

        ## Level stuff
        self.toLevel = signal("toLevel")
        self.fromLevel = signal("fromLevel")
        self.fromLevel.connect(self.gotLevelData)

        # self.levelSvg = sg.fromfile("/home/pi/rpiCarGps/GUI/Images/Level.svg")
        self.levelSvg  = etree.parse("/home/pi/rpiCarGps/GUI/Images/Level.svg")
        self.levelRoot = self.levelSvg.getroot()
        self.levelXi   = self.levelRoot.xpath("//*[@id = 'Xindicator']")[0]
        self.levelYi   = self.levelRoot.xpath("//*[@id = 'Yindicator']")[0]

        ## Radio stuff
        self.Store = False

        # Action signal to talk to main proc
        self.actionSignal = signal("Actions")

        # MPD stuff
        self.toMpd = signal("toMPD")
        self.fromMpd = signal("fromMPD")
        self.fromMpd.connect(self.gotMpdData)

        self.updateLevelSvg()
        
        window.show_all()
        myNavit.start()

    ## --------------------------------------------------------------
    ## Description : zoom/unzoom level
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 30-42-2020 10:42:05
    ## --------------------------------------------------------------
    def levelZoom(self, args):
        self.config["Level"]["zoom"]="%s"%self.builder.get_object("levelZoom").get_value()
        
    ## --------------------------------------------------------------
    ## Description : reset level
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-25-2020 20:25:53
    ## --------------------------------------------------------------
    def levelReset(self, args):
        self.toLevel.send("reset")
        
    ## --------------------------------------------------------------
    ## Description : update level svg
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-04-2020 18:04:42
    ## --------------------------------------------------------------
    def updateLevelSvg(self):
        self.builder.get_object("levelImage").clear()
        stream = Gio.MemoryInputStream.new_from_bytes(GLib.Bytes.new(etree.tostring(self.levelSvg)))
        pixbuf = GdkPixbuf.Pixbuf.new_from_stream(stream, None)
        self.builder.get_object("levelImage").set_from_pixbuf(pixbuf)
        
        
    ## --------------------------------------------------------------
    ## Description : tab focus changed
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-51-2020 15:51:51
    ## --------------------------------------------------------------
    def focusTab(self, nb,box,i):
        if (i==1):
            self.toLevel.send("start")
            print("W=%s,H=%s"%(nb.get_allocation().width,nb.get_allocation().height))
            print("W=%s,H=%s"%(box.get_allocation().width,box.get_allocation().height))
        else:
            self.toLevel.send("stop")

    ## --------------------------------------------------------------
    ## Description : treat mpd signals
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 13-06-2021 12:06:14
    ## --------------------------------------------------------------
    def gotMpdData(self, data):
        # print("MPD: received %s"%data)
        GLib.idle_add(self.builder.get_object("mpdTitle").set_text,data["title"])
        GLib.idle_add(self.builder.get_object("mpdArtist").set_text,data["artist"])
        GLib.idle_add(self.builder.get_object("mpdAlbum").set_text,data["album"])
        
    ## --------------------------------------------------------------
    ## Description : treat Level data
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 29-17-2020 16:17:00
    ## --------------------------------------------------------------
    def gotLevelData(self, data):

        print("Level")
        S = pow(10,float(self.config["Level"]["zoom"]))
        X = round(S*0.0631*data["X"]+265)
        Y = round(S*0.1071*data["Y"]+450)
        print(data)
        print("X:%s, Y:%s"%(X,Y))
        self.levelXi.set("y1","%s"%X)
        self.levelXi.set("y2","%s"%X)
        
        self.levelYi.set("x1","%s"%Y)
        self.levelYi.set("x2","%s"%Y)

        self.levelSvg.write("/home/pi/tmp/Test.svg")
        
        GLib.idle_add(self.updateLevelSvg)
        
    ## --------------------------------------------------------------
    ## Description : treat signal received from radio
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 28-31-2019 11:31:54
    ## --------------------------------------------------------------
    def gotRadioSignal (self,data):
        # print("GUI: received %s from Radio"%data)
        # for i in data:
        #     print("%s: %s"%(i,data[i]))
        GLib.idle_add(self.builder.get_object("radioFreq").set_text,
                      "%s MHz"%data["Channel"] if "Channel" in data else "")
        GLib.idle_add(self.builder.get_object("radioInfo").set_text,
                      "%s"%data["Station"] if "Station" in data else "")
        GLib.idle_add(self.builder.get_object("radioSignalStrength").set_value,
                      float(data["Strength"]))
        rDS = ""
        for c in data["rdsText"]:
            rDS+=c
        GLib.idle_add(self.builder.get_object("radioRdsText").set_text,rDS)
            
    ## --------------------------------------------------------------
    ## Description : GUI actions
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 26-06-2019 14:06:35
    ## --------------------------------------------------------------
    def Action (self,args,args2=None):
        print("mainwindow Action: %s"%args.get_name())
        if "seekUp" in args.get_name():
            self.toRadio.send("seekUp")
            # self.clearRadioData()
        elif "seekDown" in args.get_name():
            self.toRadio.send("seekDown")
            # self.clearRadioData()
        elif "radioOnOff" in args.get_name():
            self.actionSignal.send("radioOnOff")
            # self.clearRadioData()
        elif "radioStoreSelector" in args.get_name():
            self.Store = self.builder.get_object("radioStoreSelector").get_active ()
        elif "radioStore" in args.get_name():
            id = args.get_name().split("_")[1]
            if self.Store:
                self.actionSignal.send("radioStore %s"%id)
            else:
                self.actionSignal.send("radioRestore %s"%id)
        elif "mpdPlay" in args.get_name():
            print("MPD play")
            self.toMpd.send("play")
        elif "mpdSkip" in args.get_name():
            self.toMpd.send("next")
        elif "mpdPrev" in args.get_name():
            self.toMpd.send("previous")
        

    ## --------------------------------------------------------------
    ## Description : empty radion data
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-56-2021 17:56:06
    ## --------------------------------------------------------------
    def clearRadioData(self):
        print("clear radio data")
        GLib.idle_add(self.builder.get_object("radioFreq").set_text,"")
        GLib.idle_add(self.builder.get_object("radioInfo").set_text,"")
        GLib.idle_add(self.builder.get_object("radioRdsText").set_text,"")
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
            self.setStyle("GUI/Styles/%s/nightStyles.css"%self.config.get("Items","Config"))
            self.mode  = "Night"
        else:
            print("switch to day")
            navit.set_layout("Car")
            self.setStyle("GUI/Styles/%s/dayStyles.css"%self.config.get("Items","Config"))
            self.mode  = "Day"
