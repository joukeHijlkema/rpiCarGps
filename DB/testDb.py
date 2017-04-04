#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 11:33 2017
#   - Initial Version 1.0
#  =================================================
from dataBase import dataBase
import arrow
import math

db = dataBase("Jouke","!Jouke","192.168.1.13","busGps")


print "SELECT Lon,Lat,Time FROM Gps WHERE Time > '%s'"%arrow.now().replace(days=-1).format("YYYY-MM-DD HH:mm:ss")
res = db.Get("SELECT Lon,Lat,Time FROM Gps WHERE Time > '%s'"%arrow.now().replace(days=-1).format("YYYY-MM-DD HH:mm:ss"))

dist = 0.0
R = 6371  #radius of the earth in km
for i in range(len(res)-1):
    lon1 = res[i][0]
    lon2 = res[i+1][0]
    lat1 = res[i][1]
    lat2 = res[i+1][1]
    x = (lon2-lon1) * math.cos( 0.5*(lat2 + lat1) )
    y = lat2 - lat1
    dist += R * math.sqrt( x*x + y*y )

print "dist today = %s km"%dist
