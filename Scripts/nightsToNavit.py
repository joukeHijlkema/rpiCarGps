#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. sept. 14:27 2022
#   - Initial Version 1.0
#  =================================================
from fastkml import kml
import argparse
from geopy.distance import geodesic as dist

parser = argparse.ArgumentParser(description='Add trip nights to Navit')
parser.add_argument('--file', required=True, help='the trip nights to read (kml)')
args = parser.parse_args()

coordGood  = []
coordNight = []

with open("/home/pi/rpiCarGps/GPS/goodSpots.txt") as goodSpots:
    for line in goodSpots:
        items = line.split()
        lat = float(items[1])
        lon = float(items[0][3:])
        coordGood.append((lat,lon))

with open("/home/pi/rpiCarGps/GPS/spots.txt") as nights:
    for line in nights:
        items = line.split()
        lat = float(items[1])
        lon = float(items[0][3:])
        coordNight.append((lat,lon))

print(coordGood)
print(coordNight)

with open(args.file, 'rt', encoding="utf-8") as myfile:
    doc=myfile.read()
k = kml.KML()
k.from_string(doc)

fid = open("/home/pi/rpiCarGps/GPS/spots.txt",mode='a')

count = 0
for r in k.features():
    for f in r.features():
        count+=1
        lon = f.geometry.x
        lat = f.geometry.y
        print("night %s (%s,%s)"%(count,lat,lon))
        newNight = True
        for c in coordGood:
            if dist(c,(lon,lat)).kilometers<1:
                newNight = False
                break
        for c in coordNight:
            if dist(c,(lat,lon)).kilometers<1:
                newNight = False
                break
        if newNight:
            fid.write('mg:%s %s type=poi_custom0 label="spot" icon_src="spot.png"\n'%(lon,lat))
            coordNight.append((lat,lon))
        else:
            print("%s,%s already there"%(lat,lon))

fid.close()
            
        
            
