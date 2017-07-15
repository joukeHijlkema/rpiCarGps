#!/usr/bin/env python
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

db = dataBase("Jouke","!Jouke","192.168.1.23","busGps")
db.start()
time.sleep(1) ## wait for db connection

data = db.Get("SELECT * from Gps ORDER BY id")

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
p           = kml.Placemark(ns, "%s"%d[0],"%s"%d[3], 'description')
p.geometry  = Point(lon1,lon2)
f.append(p)

for d in data:
    lon2 = data[0][2]
    lat2 = data[0][1]
    
    if dist((lon1,lat1),(lon2,lat2)).kilometers>10: 
        p           = kml.Placemark(ns, "%s"%d[0],"%s"%d[3], 'description')
        p.geometry  = Point(lon2,lat2)
        f.append(p)
        lon1=lon2
        lat1=lat2

fid = open("/tmp/test.kml","w")
fid.write(root.to_string(prettyprint=True))
fid.close()
