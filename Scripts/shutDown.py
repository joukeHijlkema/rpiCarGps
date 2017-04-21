#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 18:20 2017
#   - Initial Version 1.0
#  =================================================
import os
import time
import RPi.GPIO as GPIO

def shutDown(arg):
    print "shut down : %s"%arg
    # os.system('sudo shutdown -r now')
    os.system('sudo poweroff')

GPIO.setmode(GPIO.BCM)
Pin = 5
GPIO.setup(Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Pin, GPIO.RISING, callback = shutDown)

#raw_input("wait ...")
while 1:
    time.sleep(1)
