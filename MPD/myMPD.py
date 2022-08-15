#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. janv. 16:38 2021
#   - Initial Version 1.0
#  =================================================

import threading
from time import sleep
from mpd import MPDClient
from blinker import signal

class myMPD(threading.Thread):
    """Documentation for myMPD

    """
    def __init__(self):
        super(myMPD, self).__init__()
        self.client = MPDClient()               # create self.client object
        self.client.timeout = 10                # network timeout in seconds (floats allowed), default: None
        self.client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None

        self.doIt      = True
        self.toMusic   = signal("toMPD")
        self.fromMusic = signal("fromMPD")
        
        self.toMusic.connect(self.messageReceived)
        self.Verbose = False
        
    ## --------------------------------------------------------------
    ## Description : thread loop
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 03-40-2021 16:40:40
    ## --------------------------------------------------------------
    def run(self):
        
        self.client.connect("localhost", 6600)  # connect to localhost:6600
        print(self.client.mpd_version)          # print the MPD version
        self.client.clear()
        self.client.load("All")
        self.client.shuffle()
        # self.messageReceived("play")
        
        while self.doIt:
            
            sleep(1)
            what = {"action":"update"}
            song = self.client.currentsong()
            out = {**what, **song}
            self.fromMusic.send(out)


        self.client.stop()
        sleep(1)
        self.client.close()                     # send the close command
        self.client.disconnect()    
        

    ## --------------------------------------------------------------
    ## Description : treat incomming signal
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 03-45-2021 18:45:22
    ## --------------------------------------------------------------
    def messageReceived(self, msg):
        print("MPD received %s"%msg)

        try:
            self.client.connect("localhost", 6600)
        except:
            pass
        
        if "play" in msg:
            if "stop" in self.client.status()["state"]:
                self.client.play()
            else:
                self.client.pause()
        elif "next" in msg:
            self.client.next()
        elif "previous" in msg:
            self.client.previous()
        elif "pause" in msg:
            self.client.pause()
        elif "stop" in msg:
            self.client.stop()

        what = {"action":msg}
        song = self.client.currentsong()
        out = {**what, **song}
        self.fromMusic.send(out)

        if self.Verbose:
            for i in ["artist", "title", "album"]:
                print("%s :  %s"%(i,song[i]))
            
if __name__ == '__main__':
        
    def gotData(msg):
        print('\033[2J')
        print("=========================")
        for i in msg:
            print("%s:%s"%(i,msg[i]))
        print("=========================")

    Music = myMPD()
    # signal("fromMPD").connect(gotData)
    
    Music.start()
    Music.Verbose = True
    
    while 1:
        cmd = input("next: n, previous: b, play: p, pause: w, quit: q\n")
        
        if   "n" in cmd: Music.toMusic.send("next")
        elif "b" in cmd: Music.toMusic.send("previous")
        elif "p" in cmd: Music.toMusic.send("play")
        elif "w" in cmd: Music.toMusic.send("pause")
        elif "q" in cmd: break

    Music.doIt = False
    sleep(2)
