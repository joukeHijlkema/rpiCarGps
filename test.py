#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. févr. 18:05 2021
#   - Initial Version 1.0
#  =================================================

from blinker import signal

def Info(data):
    print(data)
    
signal("fromVolumeInfo").connect(Info)
signal("fromVolume").connect(Info)

signal("fromVolumeInfo").send({"Level":3})
