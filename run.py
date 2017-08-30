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
# - distance per tank, feul consomption
# - move to python 3
# - save position on quit
## ============================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from blinker import signal

config = configparser.ConfigParser()
config.read("rpiCarGps.cfg")

# from GTK.mainGtk import mainGtk as MainWindow
from GUI.mainWindow import mainWindow as MainWindow
from GPS.myGps import Gps
from DB.dataBase import dataBase
if config.getboolean("Modules","temp"):
    from TEMP.myTemp import myTemp
    self.tempOn = True
else:
    self.tempOn = False

import os
import sys
import time

data = {}
data["GPS"]={}
data["DB"]={}
data["TEMP"]={}
data["Init"]=True

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
        data["DB"]["totDist"]  = db.dstTot
        data["Init"]=False

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
    global data
    # print(data)
    wtd                = {}
    wtd["speedMeter"]  = data["GPS"]["speed"] if "speed" in data["GPS"] else "skip"
    if self.tempOn:
        wtd["Time"]        = "{}#{}".format(data["GPS"]["time"],data["TEMP"]["Value"]) if "time" in data["GPS"] and "Value" in data["TEMP"] else "skip"
    else:
        wtd["Time"]        = "{}".format(data["GPS"]["time"]) if "time" in data["GPS"] else "skip"
    wtd["dayDist"]     = data["DB"]["dayDist"] if "dayDist" in data["DB"] else "skip"   
    wtd["tripDist"]    = data["DB"]["tripDist"] if "tripDist" in data["DB"] else "skip"   
    wtd["totDist"]     = data["DB"]["totDist"] if "totDist" in data["DB"] else "skip"    
    wtd["Altitude"]    = data["GPS"]["alt"] if "alt" in data["GPS"] else "skip"    
    wtd["Rate"]        = data["GPS"]["climb"] if "climb" in data["GPS"] else "skip"     

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
    global db
    db.Quit()
    myGps.Doit=False
    if self.tempOn: temp.Doit=False
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
## Description : day history
## NOTE : 
## -
## Author : jouke hylkema
## date   : 16-03-2017 14:03:11
## --------------------------------------------------------------
def dayHist(offset):
    data["DB"]["dayDist"]  = db.dayDist(offset)    
    
real=("armv7l" in os.uname()[4])
rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
#print "root = %s"%rootPath
# win = MainWindow(1024,600,"%s/GTK/Styles.css"%rootPath,real)
win = MainWindow()
#time.sleep(1)
    
# GPS
myGps = Gps(real)
myGps.start()
while myGps.init:
    time.sleep(0.1)
    
# Database
db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)

# Temperature
if self.tempOn:
    temp = myTemp(real)
    temp.start()

#Signaling
gpsData = signal('Gps')
gpsData.connect(gotGpsData)

if self.tempOn:
    tempData = signal("Temp")
    tempData.connect(gotTempData)

resetTripSignal = signal("tripDist_return")
resetTripSignal.connect(resetTrip)

backDayTot = signal("dayTot")
backDayTot.connect(dayHist)

win.connect("delete-event",Quit)
# win.quitButton.connect("clicked", Quit)
win.builder.get_object("quitButton").connect("clicked", Quit)

GObject.timeout_add(100, timedUpdate)

print("start mainloop")
Gtk.main()


