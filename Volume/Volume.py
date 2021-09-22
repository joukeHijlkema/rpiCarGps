#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - ven. févr. 18:17 2021
#   - Initial Version 1.0
#  =================================================
import threading
from blinker import signal
import RPi.GPIO as GPIO
from time import sleep
# import alsaaudio
import pulsectl

class myVolume(threading.Thread):
    """Documentation for myVolume

    """
    def __init__(self):
        super(myVolume, self).__init__()

        self.fromVolume     = signal("fromVolume")
        self.fromVolumeInfo = signal("fromVolumeInfo")
        GPIO.setmode(GPIO.BOARD)

        self.Doit = True
        self.SW   = 11
        self.CLK  = 13
        self.SD   = 37

        self.state = 0

        GPIO.setup(self.SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.SD, GPIO.IN, pull_up_down=GPIO.PUD_UP)

             
    def run(self):
        GPIO.add_event_detect(self.CLK, GPIO.FALLING,callback=self.detectClk)
        GPIO.add_event_detect(self.SW, GPIO.BOTH,callback=self.detectSw, bouncetime=500)
        while self.Doit:
            sleep(1)
        
        GPIO.cleanup()
        print("Volume stopped")
   
    def detectClk(self,arg):
        self.state = self.state << 2
        self.state = self.state | GPIO.input(self.SD) << 1
        self.state = self.state | GPIO.input(self.CLK)
        self.state = self.state & 15

        if self.state in [10,8,2]:
            self.fromVolume.send("UP")
            
        if self.state in [0,3,12]:
            self.fromVolume.send("DOWN")

            
    def detectSw(self,arg):
        self.fromVolume.send("MUTE")
        
        

if __name__ == '__main__':

    def alsaData(data):
        global myAlsa
        step = 2
        print("received: %s"%data)
        V = myAlsa.getvolume()
        if "UP" in data:
            myAlsa.setvolume(min(100,V[0]+step))
        elif "DOWN" in data:
            myAlsa.setvolume(max(0,V[0]-step))
        elif "MUTE" in data:
            if (myAlsa.getmute() == [0,0]):
                myAlsa.setmute(1)
            else:
                myAlsa.setmute(0)
            
    def pulseData(data):
        with pulsectl.Pulse('volume-increaser') as pulse:
            sink   = pulse.sink_list()[1]
            volume = pulse.volume_get_all_chans(sink)
            if "UP" in data and volume < 1.5:
                pulse.volume_change_all_chans(sink, 0.05)
            elif "DOWN" in data and volume > 0.0:
                pulse.volume_change_all_chans(sink, -0.05)
            elif "MUTE" in data:
                V = not sink.mute
                pulse.mute(sink,V)
    
    # signal("fromVolume").connect(alsaData)
    signal("fromVolume").connect(pulseData)

    # myAlsa = alsaaudio.Mixer(control='Digital', cardindex=0)
    # myAlsa.setvolume(50)
    
    
    v = myVolume()
    v.start()

    input("hit RET to stop")
    v.Doit = False
