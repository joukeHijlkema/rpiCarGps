#!/usr/bin/env python3
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
from systemd import journal

def shutDown(arg):
    global Pin
    time.sleep(2)
    if GPIO.input(Pin):
        journal.send(
            message="JOUKE: Shutting down",
            priority=journal.Priority.INFO,
            some_field='a value',
        )
        os.system('sudo poweroff')

    
GPIO.setmode(GPIO.BCM)
Pin = 5
GPIO.setup(Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(Pin, GPIO.RISING, callback = shutDown)

while 1:
    time.sleep(1)

