#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. août 13:12 2019
#   - Initial Version 1.0
#  =================================================
from .myRadio import myRadio

def printData(data):
    for d in data:
        print("%s: %s"%(d,data[d]))

signal("fromRadio").connect(printData)

r = myRadio(87.9,0x10,1)
r.start()

while 1:
    cmd = input("Press key (u=search up, d=search down, q=quit): ")
    if "q" in cmd.lower():
        q.set()
        break
    elif "u" in cmd.lower():
        r.tuner.search(1)
    elif "d" in cmd.lower():
        r.tuner.search(0)


r.Doit = Flase
print("quitting")
time.sleep(2)
