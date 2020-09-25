#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. août 14:26 2020
#   - Initial Version 1.0
#  =================================================
from Level.myLevel import myLevel
import time
from blinker import signal
import configparser

config = configparser.ConfigParser()
config.read("/home/pi/rpiCarGps/rpiCarGps.cfg")

def gotLevelData(levelData):
    print("X:%s, Y:%s"%(levelData["X"],levelData["Y"]))

Z = eval(config.get("Params","levelZero"))    
L = myLevel(Z[0],Z[1])
L.start()

signal("fromLevel").connect(gotLevelData)
toLevel = signal("toLevel")

while True:
 I=input("hit q to stop, els send to level: ")
 if "q" in I:
     break
 toLevel.send(I)
 
L.Doit = False

config["Params"]["levelZero"]="[%s,%s]"%(10,20)
with open('/tmp/test.cfg', 'w') as configfile:
    config.write(configfile)
