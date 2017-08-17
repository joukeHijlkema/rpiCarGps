#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 15:35 2017
#   - Initial Version 1.0
#  =================================================
import sys
sys.path.append("../DB")
import time
from dataBase import dataBase

db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)

db.Exec("REPLACE INTO Memory (Id,What,Value) VALUES (1,'Day',%s)"%db.dayDist(0))
db.Exec("REPLACE INTO Memory (Id,What,Value) VALUES (2,'Trip',%s)"%db.tripDist())
db.Exec("REPLACE INTO Memory (Id,What,Value) VALUES (3,'Total',%s)"%db.totDist())

db.Quit()

