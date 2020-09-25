#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. août 17:05 2017
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
from geopy.distance import geodesic as dist

parser = argparse.ArgumentParser(description='Extract a journey from th rpiGps')

parser.add_argument('--start', required=True, help='start date of the form YYYY-MM-DD')
parser.add_argument('--stop' , required=True, help='stop date of the form YYYY-MM-DD')
parser.add_argument('--title' , required=True, help='title of the trip')
parser.add_argument('--subTitle' , required=True, help='subtitle of the trip')
args = parser.parse_args()

db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)

data = db.Get("SELECT Id,Lat,Lon,Time from Gps WHERE Time BETWEEN '{}' AND '{}' ORDER BY id".format(args.start,args.stop))
print("SELECT Id,Lat,Lon,Time from Gps WHERE Time BETWEEN '{}' AND '{}' ORDER BY id".format(args.start,args.stop))
print("found %s items"%len(data))

# Create the root KML object
rootNights  = kml.KML()
rootRoute   = kml.KML()
ns          = '{http://www.opengis.net/kml/2.2}'

# Create a KML Document and add it to the KML root object
docNights  = kml.Document(ns, '1', "nuits-%s"%args.title, args.subTitle)
rootNights.append(docNights)

docRoute  = kml.Document(ns, '1', "route-%s"%args.title, args.subTitle)
rootRoute.append(docRoute)

t1 = arrow.get(data[0][3])
lat=data[0][1]
lon=data[0][2]
id = 0
for d in data:
    t2 = arrow.get(d[3])
    if t2>t1.ceil("day"):
        id+=1
        print("found night {}".format(id))
        p = kml.Placemark(ns, "%s"%id,"nuit_%s"%id, "nuit numéro %s"%id)
        p.geometry  = Point(lon,lat)
        docNights.append(p)
        t1 = t2
    lat=d[1]
    lon=d[2]
lat=data[0][1]
lon=data[0][2]
id = 0
for d in data:
    # print(dist((d[2],d[1]),(lon,lat)).kilometers)
    if dist((d[2],d[1]),(lon,lat)).kilometers>10:
        p = kml.Placemark(ns, "%s"%id,"km_%s"%id, "borne numéro %s"%id)
        p.geometry  = Point(lon,lat)
        docRoute.append(p)
        lat=d[1]
        lon=d[2]

fid = open("{}_nights.kml".format(args.title),"w")
fid.write(rootNights.to_string(prettyprint=True))
fid.close()

fid = open("{}_route.kml".format(args.title),"w")
fid.write(rootRoute.to_string(prettyprint=True))
fid.close()


