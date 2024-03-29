#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. mai 17:09 2017
#   - Initial Version 1.0
#  =================================================
from DB.dataBase import dataBase
import time
from fastkml import kml
from lxml import etree
from shapely.geometry import Point, LineString, Polygon
from geopy.distance import vincenty as dist

date = input("start date dd/mm/yyyy ? ")

db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)

data = db.Get("SELECT Id,Lat,Lon,Time from Gps WHERE Time >= '%s' ORDER BY id"%date)
# print(data)

# Create the root KML object
root = kml.KML()
ns = '{http://www.opengis.net/kml/2.2}'

# Create a KML Document and add it to the KML root object
doc = kml.Document(ns, '1', 'test document', 'test gps data extraction')
root.append(doc)
# Create a KML Folder and nest it in the first Folder
f = kml.Folder(ns, 'nested-fid', 'nested f name', 'nested f description')
doc.append(f)

lon1 = data[0][2]
lat1 = data[0][1]
p           = kml.Placemark(ns, "0","%s"%data[0][3], 'description')
p.geometry  = Point(lon1,lat1)
f.append(p)

for d in data:
    lon2 = d[2]
    lat2 = d[1]
    print(dist((lon1,lat1),(lon2,lat2)).kilometers)
    if dist((lon1,lat1),(lon2,lat2)).kilometers>10: 
        p           = kml.Placemark(ns, "%s"%d[0],"%s"%d[3], 'description')
        p.geometry  = Point(lon2,lat2)
        f.append(p)
        lon1=lon2
        lat1=lat2

fid = open("/tmp/test.kml","w")
fid.write(root.to_string(prettyprint=True))
fid.close()
