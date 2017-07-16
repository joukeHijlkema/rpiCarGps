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
## - Add altitude
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

data = {}
data["GPS"]={}
data["DB"]={}
data["TEMP"]={}

## --------------------------------------------------------------
## Description : act on gps data
## NOTE : 
## -
## Author : jouke hylkema
## date   : 03-04-2017 10:04:28
## --------------------------------------------------------------
def gotGpsData(gpsData):
    global data,db

    print("Got GPS data data= %s" %gpsData)
    data["GPS"] = gpsData
    db.addPoint(gpsData)
    data["DB"]["dayDist"] = db.dayDist(back=2)
    data["DB"]["totDist"] = db.totDist()

## --------------------------------------------------------------
## Description : got temperature reading
## NOTE : 
## -
## Author : jouke hylkema
## date   : 03-12-2017 22:12:01
## --------------------------------------------------------------
def gotTempData (tempData):
    global data
    print "temp = %s C"%tempData
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
        signal("totDist").send(data["DB"]["totDist"])
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
    myGps.Doit=False
    temp.Doit=False
    Gtk.main_quit()

real=("armv7l" in os.uname()[4])
rootPath = os.path.dirname(os.path.realpath(sys.argv[0]))
print "root = %s"%rootPath
win = MainWindow(1024,600,"%s/GTK/Styles.css"%rootPath,real)
# win = MainWindow(1024,600,"./GTK/Styles.css",real)
    
# GPS
myGps = Gps(real)
myGps.start()

# Database
db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()

# Temperature
temp = myTemp(real)
temp.start()

#Signaling
gpsData = signal('Gps')
gpsData.connect(gotGpsData)
tempData = signal("Temp")
tempData.connect(gotTempData)

win.connect("delete-event",Quit)
win.quitButton.connect("clicked", Quit)

GObject.timeout_add(1000, timedUpdate)

print "start mainloop"
Gtk.main()


