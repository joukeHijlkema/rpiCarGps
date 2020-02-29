#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. août 16:30 2019
#   - Initial Version 1.0
#  =================================================

import RPi.GPIO as GPIO
# from smbus2 import SMBusWrapper,i2c_msg
import time
import subprocess
import busio
import board
import struct

def Read(i2c):
    result = bytearray(32)
    i2c.readfrom_into(0x10, result)

    out = [0x0000 for i in range(16)]

    for i in range(16):
        id = (10+i)%16
        r = result[2*i]<<8|result[2*i+1]
        out[id] = r

    for id,r in enumerate(out):
        print("reg %d: %s (%s)"%(id,format(r,'016b'),format(r,'04x')))
    return out
    
def Write(i2c,buf):
    out = struct.pack(">6H",*buf[2:8])
    i2c.writeto(0x10,out)
        

print("bit bang receiver")
res        = 23
sdio       = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(res,GPIO.OUT)
GPIO.setup(sdio,GPIO.OUT)

GPIO.output(sdio,GPIO.LOW)
time.sleep(0.1)
GPIO.output(res,GPIO.LOW)
time.sleep(0.1)
GPIO.output(res,GPIO.HIGH)
time.sleep(0.1)
subprocess.check_output(['gpio', '-g', 'mode', '2', 'ALT0'])

i2c = busio.I2C(board.SCL, board.SDA)
buf = Read(i2c)
buf[7] = 0x8100
Write(i2c,buf)
Read(i2c)

    
