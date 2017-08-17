#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. avril 16:24 2017
#   - Initial Version 1.0
#  =================================================
## ========= TODO =============

## ============================

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from blinker import signal

from GTK.mainGtk import mainGtk as MainWindow
from GPS.myGps import Gps
from DB.dataBase import dataBase
from TEMP.myTemp import myTemp

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
#    print gpsData
    data["GPS"] = gpsData
    if db.addPoint(gpsData) or data["Init"]:
        data["DB"]["dayDist"]  = db.dstDay
        data["DB"]["tripDist"] = db.dstTrip
        data["DB"]["totDist"]  = db.dstTot
        #print(data["DB"])
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
    # print "temp = %s C"%tempData
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
    try:
        signal("speedMeter").send(data["GPS"]["speed"])
        signal("Time").send("%s#%s"%(data["GPS"]["time"],data["TEMP"]["Value"]))
        signal("dayDist").send(data["DB"]["dayDist"])
        signal("tripDist").send(data["DB"]["tripDist"])
        signal("totDist").send(data["DB"]["totDist"])
        signal("alt").send(data["GPS"]["alt"])
        signal("rate").send(data["GPS"]["climb"])
    except:
        print "not all data worked"
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
    temp.Doit=False
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
win = MainWindow(1024,600,"%s/GTK/Styles.css"%rootPath,real)
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
temp = myTemp(real)
temp.start()

#Signaling
gpsData = signal('Gps')
gpsData.connect(gotGpsData)

tempData = signal("Temp")
tempData.connect(gotTempData)

resetTripSignal = signal("tripDist_return")
resetTripSignal.connect(resetTrip)

backDayTot = signal("dayTot")
backDayTot.connect(dayHist)

win.connect("delete-event",Quit)
win.quitButton.connect("clicked", Quit)

GObject.timeout_add(100, timedUpdate)

print "start mainloop"
Gtk.main()


