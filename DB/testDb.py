#!/usr/bin/env python3
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
import time

db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()
while db.init:
    time.sleep(0.1)

print(db.dstDay)
print(db.dstTrip)
print(db.dstTot)
