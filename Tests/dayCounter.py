#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. avril 16:24 2017
#   - Initial Version 1.0
#  =================================================
import sys
sys.path.insert(0,"../DB")
from dataBase import dataBase

import time

db = dataBase("Jouke","!Jouke","localhost","busGps")
db.start()

while db.init:
    time.sleep(1)
d=db.dayDist()
print d    
d=db.dayDist(back=1)
print d    
d=db.dayDist(back=2)
print d    
d=db.dayDist(back=3)
print d    
d=db.dayDist(back=4)
print d    
