#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mar. août 14:55 2019
#   - Initial Version 1.0
#  =================================================
import RPi.GPIO as GPIO
import time
import subprocess
import busio
import board
import struct
from blinker import signal

from Classes.myRdsPiCodes import piCodes

class mySi4703(object):
    """Documentation for mySi4703"""
    def __init__(self,i2c_address,i2c_bus):
        super(mySi4703, self).__init__()
        self.i2c_address = i2c_address
        self.i2c_bus     = i2c_bus
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.res         = 23
        self.sdio        = 2
        self.gpio2       = 22
        GPIO.setup(self.res,GPIO.OUT)
        GPIO.setup(self.sdio,GPIO.OUT)
        GPIO.setup(self.gpio2,GPIO.IN)

        self.keys = {
            "XOSEN"       : (7,[15]),
            "DMUTE"       : (2,[14]),
            "SEEK"        : (2,[8]),
            "SEEKUP"      : (2,[9]),
            "SKMODE"      : (2,[10]),
            "DISABLE"     : (2,[6]),
            "ENABLE"      : (2,[0]),
            "TUNE"        : (3,[15]),
            "CHANNEL"     : (3,[9,8,7,6,5,4,3,2,1,0]),
            "RDSIEN"      : (4,[15]),
            "RDS"         : (4,[12]),
            "DE"          : (4,[11]),
            "BAND"        : (5,[7,6]),
            "SPACE"       : (5,[5,4]),
            "VOLUME"      : (5,[3,2,1,0]),
            "STC"         : (10,[14]),
            "READCHANNEL" : (11,[9,8,7,6,5,4,3,2,1,0])
        }

        self.data = {}
        
        self.Buffer = [0x0000 for i in range(16)]
        self.i2c    = busio.I2C(board.SCL, board.SDA)
        self.PI     = piCodes()

        self.newData = signal('Tuner')

        self.init()
        
        print("done")

    ## --------------------------------------------------------------
    ## Description : init the device
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 22-38-2019 15:38:40
    ## --------------------------------------------------------------
    def init (self):
        print("bit bang receiver")
        GPIO.output(self.sdio,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.res,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.res,GPIO.HIGH)
        time.sleep(0.1)
        subprocess.check_output(['gpio', '-g', 'mode', '2', 'ALT0'])

        self.Read() # to initialise the buffer
        self.Info("Init regs")

        self.Set("XOSEN",1)
        self.Write()
        self.Read()
        time.sleep(0.6)
        
        self.Set("DMUTE",1)
        self.Set("DISABLE",0)
        self.Set("ENABLE",1)
        self.Set("RDS",1)
        self.Set("DE",1)
        self.Set("BAND",[0,0])
        self.Set("SPACE",[0,1])
        self.Set("VOLUME",[1,1,1,1])
        self.Write()
        self.Read()
       
    ## --------------------------------------------------------------
    ## Description : set keyword
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-28-2019 14:28:13
    ## --------------------------------------------------------------
    def Set (self,key,values):
        if type(values) != list:
            values = [values]
        if key in self.keys:
            reg  = self.keys[key][0]
            bits = self.keys[key][1]
            self.setBit(reg,bits,values)

    ## --------------------------------------------------------------
    ## Description : get a range of bits
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-14-2019 15:14:51
    ## --------------------------------------------------------------
    def Get (self,key):
        reg       = self.keys[key][0]
        start     = 15-self.keys[key][1][0]
        end       = 15-self.keys[key][1][-1]+1 ## remeber slices are exlusive

        rs = bin(self.Buffer[reg])[2:].zfill(16)
        return int(rs[start:end],2)
        
        
    ## --------------------------------------------------------------
    ## Description : Quit
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 23-54-2019 15:54:11
    ## --------------------------------------------------------------
    def Quit (self):
        GPIO.output(self.res,GPIO.LOW)
        time.sleep(0.1)

    ## --------------------------------------------------------------
    ## Description : set the frequency
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 23-26-2019 15:26:59
    ## --------------------------------------------------------------
    def setFrequency (self,frequency):
        self.Read()

        self.Set("CHANNEL",self.freq2chan(frequency))
        self.Set("TUNE",1)
        self.Write()
        print(" tuning ...")
        GPIO.wait_for_edge(self.gpio2, GPIO.RISING)
        
        self.Read()
        self.Info("after set frequency to %s"%frequency)
        self.Set("TUNE",0)
        self.Write()

        self.doRds()

    ## --------------------------------------------------------------
    ## Description : search
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 26-39-2019 11:39:22
    ## --------------------------------------------------------------
    def search (self,dir):
        self.Set("SEEKUP",dir)
        self.Set("SKMODE",0)
        self.Set("SEEK",1)
        self.Write()
        print(" seeking ...")
        GPIO.wait_for_edge(self.gpio2, GPIO.RISING)

        self.Read()
        self.Set("SEEK",0)
        self.Set("STC",0)
        self.Write()
        
        self.doRds()
        
    ## --------------------------------------------------------------
    ## Description : do the RDS thing
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-01-2019 16:01:19
    ## --------------------------------------------------------------
    def doRds (self):
        # wait for RDS data
        self.Set("RDSIEN",1)
        self.Write()
        print(" RDS ...")
        GPIO.wait_for_edge(self.gpio2, GPIO.RISING)
        self.Read()

        self.Info("RDS")
        self.data["Channel"] = self.chan2freq(RDS=True)
        self.data["Station"] = self.PI.getStation(format(self.Buffer[12],'04x'))
        self.newData.send(self.data)
        print("Channel: %s MHz"%self.data["Channel"])
        print("Station: %s"%self.data["Station"])

    ## --------------------------------------------------------------
    ## Description : frequency to channel conversion
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-58-2019 14:58:16
    ## --------------------------------------------------------------
    def freq2chan (self,frequency):
        channel = int(round(10*(frequency - 87.5)))
        bits    = [0 for i in range(10)]
        nb      = len(bin(channel))-2
        for i,b in enumerate(reversed(bin(channel)[2:])):
            bits[9-i] = int(b)
        return bits

    ## --------------------------------------------------------------
    ## Description : chan2freq
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 24-02-2019 15:02:12
    ## --------------------------------------------------------------
    def chan2freq (self,RDS=False):
        if RDS:
            chan = self.Get("READCHANNEL")
        else:
            chan = self.Get("CHANNEL")
        freq = 0.1*chan+87.5
        return freq
        
    ## --------------------------------------------------------------
    ## Description : write to the buffer
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 21-58-2019 10:58:07
    ## --------------------------------------------------------------
    def Write (self):
        out = struct.pack(">6H",*self.Buffer[2:8])
        self.i2c.writeto(0x10,out)
        time.sleep(0.1)
        
    ## --------------------------------------------------------------
    ## Description : Read the registers
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 21-27-2019 12:27:49
    ## --------------------------------------------------------------
    def Read (self):
        time.sleep(0.1)
        result = bytearray(32)
        self.i2c.readfrom_into(0x10, result)
        for i in range(16):
            id = (10+i)%16
            self.Buffer[id] = result[2*i]<<8|result[2*i+1]
        
    ## --------------------------------------------------------------
    ## Description : Print info
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 21-04-2019 11:04:00
    ## --------------------------------------------------------------
    def Info (self,msg="UNKNOWN"):
        print("=== %s ==="%msg)
        for n,i in enumerate(self.Buffer):
            print("Register %2s : %s (0x%s)"%(n,format(i,'016b'),format(i,'04x')))
        print("==========")

    ## --------------------------------------------------------------
    ## Description : set bit in register
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 21-10-2019 12:10:34
    ## --------------------------------------------------------------
    def setBit (self,reg,index,value):
        if len(index) != len(value):
            raise("number of bits and values don't match")
        for i,b in enumerate(index):
            if value[i]==1:
                self.Buffer[reg] |= 1 << b
            else:
                self.Buffer[reg] &= ~(1 << b)

    ## --------------------------------------------------------------
    ## Description : get bits
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 23-15-2019 16:15:28
    ## --------------------------------------------------------------
    def getBit (self,reg,index):
        return int(bin(self.Buffer[reg][2:][-(index)]))
