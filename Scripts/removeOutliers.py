#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. juil. 16:17 2019
#   - Initial Version 1.0
#  =================================================
import sys
sys.path.append("../DB")
import time
from dataBase import dataBase
import argparse
import arrow
from fastkml import kml
from shapely.geometry import Point
from geopy.distance import vincenty as dist
db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)
data = db.Get("SELECT Id,Lat,Lon,Time from Gps ORDER BY id")
print("found %s items"%len(data))

lat=data[0][1]
lon=data[0][2]
id = 0
big = 100

for d in data:
    D = dist((d[2],d[1]),(lon,lat)).kilometers
    if D>big:
        print("point %d has a distance of %s km"%(d[0],D))
        yn = input("Delete it ? (y/n) ")
        if "y" in yn:
            db.Exec("DELETE FROM `Gps` WHERE `Gps`.`ID` = %s"%d[0])
            print("DELETE FROM `Gps` WHERE `Gps`.`ID` = %s"%d[0])
    else:        
        lat=d[1]
        lon=d[2]
