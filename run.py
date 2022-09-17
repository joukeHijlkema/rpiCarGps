#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. avril 16:24 2017
#   - Initial Version 1.0
#  =================================================
## ========= TODO =============
# - average speed
# - distance per tank, fuel consomption
## ============================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GLib
print(Gtk.get_major_version ())
print(Gtk.get_minor_version ())
print(Gtk.get_micro_version ())
from blinker import signal
import configparser

# to get rid off the arrow warnings
import warnings
# from arrow.factory import ArrowParseWarning
# warnings.simplefilter("ignore", ArrowParseWarning)
config = configparser.ConfigParser()
config.read("/home/pi/rpiCarGps/rpiCarGps.cfg")

# from GTK.mainGtk import mainGtk as MainWindow
from GUI.mainWindow import mainWindow as MainWindow
from GPS.myGps import Gps
from DB.dataBase import dataBase
from MPD.myMPD import myMPD

if config.getboolean("Modules","temp"):
    from TEMP.myTemp import myTemp
    tempOn = True
else:
    tempOn = False

if config.getboolean("Modules","radio"):
    from Radio.myRadio import myRadio as Radio
    radioOn = True
    radio   = None
else:
    radioOn = False

if config.getboolean("Modules","level"):
    from Level.myLevel import myLevel
    levelOn = True
else:
    levelOn = False
    
import os
import sys
import time
import math

data = {}
data["GPS"]={}
data["DB"]={}
data["TEMP"]={}
data["Init"]=True
data["Radio"]={}

## --------------------------------------------------------------
## Description : Act on level data
## NOTE : 
## -
## Author : jouke hylkema
## date   : 29-04-2020 15:04:34
## --------------------------------------------------------------
def gotLevelData(levelData):
    if "raz" in levelData:
        config["Level"]["zero"]="[%s,%s]"%(levelData[1],levelData[2])
        
    
## --------------------------------------------------------------
## Description : act on gps data
## NOTE : 
## -
## Author : jouke hylkema
## date   : 03-04-2017 10:04:28
## --------------------------------------------------------------
def gotGpsData(gpsData):
    global data,db,win
    # print(gpsData)
    data["GPS"] = gpsData
    if db.addPoint(gpsData) or data["Init"]:
        data["DB"]["dayDist"]  = db.dstDay
        data["DB"]["tripDist"] = db.dstTrip
        data["DB"]["tankDist"] = db.dstTank
        data["DB"]["totDist"]  = db.dstTot
        data["Init"]=False

## --------------------------------------------------------------
## Description : got radio info
## NOTE : 
## -
## Author : jouke hylkema
## date   : 26-52-2019 14:52:24
## --------------------------------------------------------------
def gotRadioData (radioData):
    # print("RADIO: got %s"%radioData)
    for i in ["Channel","Station"]:
        data["Radio"][i]=radioData[i]
        config["Radio"][i] = "%s"%radioData[i]
## --------------------------------------------------------------
## Description : got temperature reading
## NOTE : 
## -
## Author : jouke hylkema
## date   : 03-12-2017 22:12:01
## --------------------------------------------------------------
def gotTempData (tempData):
    global data
    # print("temp = %s C"%tempData)
    data["TEMP"]["Value"] = tempData
    
## --------------------------------------------------------------
## Description : timed update to see if this avoids updates freezing
## NOTE : This seems to work !! Directly updating might give a race condition ?
## -
## Author : jouke hylkema
## date   : 03-42-2017 10:42:09
## --------------------------------------------------------------
def timedUpdate ():
    # print(data)
    wtd                = {}
    wtd["speedMeter"]  = data["GPS"]["speed"] if "speed" in data["GPS"] else "skip"
    if tempOn:
        wtd["Time"]        = "{}#{}".format(data["GPS"]["time"],data["TEMP"]["Value"]) if "time" in data["GPS"] and "Value" in data["TEMP"] else "skip"
    else:
        wtd["Time"]        = "{}".format(data["GPS"]["time"]) if "time" in data["GPS"] else "skip"
    wtd["dayDist"]     = data["DB"]["dayDist"] if "dayDist" in data["DB"] else "skip"   
    wtd["tripDist"]    = data["DB"]["tripDist"] if "tripDist" in data["DB"] else "skip"   
    wtd["tankDist"]    = data["DB"]["tankDist"] if "tankDist" in data["DB"] else "skip"   
    wtd["totDist"]     = data["DB"]["totDist"] if "totDist" in data["DB"] else "skip"    
    wtd["Altitude"]    = data["GPS"]["alt"] if "alt" in data["GPS"] else "skip"    
    wtd["Rate"]        = 2.0*math.atan2(data["GPS"]["climb"],data["GPS"]["speed"])/math.pi if ("climb" in data["GPS"] and "speed" in data["GPS"]) else ["skip"]

    for what in wtd:
        if wtd[what]=="skip": continue
        try:
            # print("what={}, value={}".format(what,wtd[what]))
            signal(what).send(wtd[what])
        except:
            # print("{} did not work".format(what))
            pass
    return True

## --------------------------------------------------------------
## Description : Quit
## NOTE : 
## -
## Author : jouke hylkema
## date   : 03-05-2017 10:05:20
## --------------------------------------------------------------
def Quit(*args):
    global radio,db,tempOn,myGps,temp,Music
    print("Quitting")
    db.Quit()
    myGps.Doit=False
    Music.Doit=False    
    if tempOn:
        print("kill temp")
        temp.Doit=False
    if radioOn:
        print("kill radio")
        if radio:
            radio.Doit=False
    if levelOn:
        print("kill level")
        level.Doit=False
    with open("/home/pi/rpiCarGps/rpiCarGps.cfg", 'w') as configfile:
        config.write(configfile)
    Gtk.main_quit()

## --------------------------------------------------------------
## Description : reset the trip
## NOTE : 
## -
## Author : jouke hylkema
## date   : 16-03-2017 14:03:11
## --------------------------------------------------------------
def resetTrip (data):
    global db
    print("reset trip in run")
    db.resetTrip()
    
## --------------------------------------------------------------
## Description : reset the tank
## NOTE : 
## -
## Author : jouke hylkema
## date   : 16-03-2017 14:03:11
## --------------------------------------------------------------
def resetTank (data):
    global db
    print("reset tank in run")
    db.resetTank()
    
## --------------------------------------------------------------
## Description : day history
## NOTE : 
## -
## Author : jouke hylkema
## date   : 16-03-2017 14:03:11
## --------------------------------------------------------------
def dayHist(offset):
    data["DB"]["dayDist"]  = db.dayDist(offset)    

## --------------------------------------------------------------
## Description : Actions from the GUI
## NOTE : 
## -
## Author : jouke hylkema
## date   : 26-37-2019 13:37:17
## --------------------------------------------------------------
def Actions (args):
    global radio, config
    #print("Actions: %s"%args)
    #print("radioOn = %s"%radioOn)
    if radioOn:
        if "radioOnOff" in args:
            if radio is not None:
                radio.Doit = False
                radio = None
            else:
                radio = Radio(config.getfloat("Radio","lastfreq"),0x10,1)
                radio.start()
        elif "radioStore" in args and radio is not None:
            config["Radio"]["preset_%s"%args.split()[1]] = "%s"%radio.getFreq()
        elif "radioRestore" in args and radio is not None:
            radio.setFrequency(config.getfloat("Radio","preset_%s"%args.split()[1]))
    if "save" in args:
        with open("/home/pi/rpiCarGps/rpiCarGps.cfg", 'w') as configfile:
            config.write(configfile)
    if "goodSpot" in args:
        with open("/home/pi/rpiCarGps/GPS/goodSpots.txt", 'a') as goodspotFile:
            goodspotFile.write('mg:%s %s type=poi_custom0 label="good spot" icon_src="camping.png"\n'%
                               (data["GPS"]["lon"],data["GPS"]["lat"]))
            goodspotFile.close()
## --------------------------------------------------------------
## Description : got MPD data
## NOTE : 
## -
## Author : jouke hylkema
## date   : 27-15-2021 15:15:26
## --------------------------------------------------------------
def gotMpdData(args):
    #print("received from MPD: %s"%args)
    pass
            
## =========================================================
## MAIN

real=("armv7l" in os.uname()[4])
### begin debug ###
# real = False
### end debug   ###


rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
print("root = %s"%rootPath)
# win = MainWindow(1024,600,"%s/GTK/Styles.css"%rootPath,real)
win = MainWindow(config)
#time.sleep(1)
print("Main window done")

# GPS
myGps = Gps(real)
myGps.start()
while myGps.init:
    time.sleep(0.1)
print("GPS done")
    
# Database
db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)
print("Database done")

# Temperature
if tempOn:
    temp = myTemp(real)
    temp.start()
    print("Temp done")

#level
if levelOn:
    Z = eval(config.get("Level","zero"))
    level = myLevel(Z[0],Z[1])
    level.start()
    signal("fromLevel").connect(gotLevelData)
    print("Level started")

# MPD
Music = myMPD()
Music.start()

#Signaling
signal('Gps').connect(gotGpsData)

if tempOn:
    signal("Temp").connect(gotTempData)

if radioOn:
    signal("fromRadio").connect(gotRadioData)

signal("tripDist_return").connect(resetTrip)

signal("tankDist_return").connect(resetTank)

signal("dayTot").connect(dayHist)

signal("Actions").connect(Actions)

signal("fromMPD").connect(gotMpdData)

win.connect("delete-event",Quit)
win.builder.get_object("quitButton").connect("clicked", Quit)

GLib.timeout_add(100, timedUpdate)
print("Signaling done")

print("start mainloop")
Gtk.main()

print("save data")
db.addPoint(data["GPS"],Force=True)
db.Quit()
Music.doIt = False

