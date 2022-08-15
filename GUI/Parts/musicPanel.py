#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - mer. août 11:13 2021
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from blinker import signal

class musicPanel(Gtk.Grid):
    """Documentation for musicPanel

    """
    def __init__(self,parent,*args,**kw):
        super(musicPanel, self).__init__()

        
        self.parent = parent
        self.w      = kw["w"] if "w" in kw else 324
        self.h      = kw["h"] if "h" in kw else 20
        self.name   = kw["name"] if "name" in kw else "noName"
        print("kw = %s"%kw)
        print("h = %s"%self.h)
        self.set_size_request(self.w,self.h)
        self.set_row_spacing(2)
        self.set_column_spacing(2)
        self.set_column_homogeneous(True)

        self.toMpd = signal("toMPD")

        self.play       = Gtk.Button.new()
        self.play.connect("clicked",self.playAction)
        self.play.set_name("musicPanelPlay")
        self.playImage  = Gtk.Image()
        self.playImage.set_from_stock(Gtk.STOCK_MEDIA_PLAY, Gtk.IconSize.DND);
        self.pauseImage = Gtk.Image()
        self.pauseImage.set_from_stock(Gtk.STOCK_MEDIA_PAUSE, Gtk.IconSize.DND);
        self.play.set_image(self.playImage)
    
        self.next      = Gtk.Button.new()
        self.next.connect("clicked",self.nextAction)
        self.next.set_name("musicPanelNext")
        self.nextImage = Gtk.Image()
        self.nextImage.set_from_stock(Gtk.STOCK_MEDIA_NEXT, Gtk.IconSize.DND);
        self.next.set_image(self.nextImage)
       
        self.artist = Gtk.Label(label="Artist")
        self.artist.set_name("musicPanelArtist")
        self.artist.set_justify(Gtk.Justification.LEFT)

        self.song = Gtk.Label(label="Song")
        self.song.set_name("musicPanelSong")
        self.song.set_justify(Gtk.Justification.LEFT)
        
#        self.pack_start(self.play,True,True,2)
#        self.pack_start(self.next,True,True,2)

        self.attach(self.artist,0,0,2,1)
        self.attach(self.song,0,1,2,1)
        self.attach(self.play,0,2,1,1)
        self.attach(self.next,1,2,1,1)

        
    ## --------------------------------------------------------------
    ## Description : play action
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 11-32-2021 11:32:03
    ## --------------------------------------------------------------
    def playAction(self, args):
        self.toMpd.send("play")
        
    ## --------------------------------------------------------------
    ## Description : nextAction
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 11-33-2021 11:33:17
    ## --------------------------------------------------------------
    def nextAction(self, args):
        self.toMpd.send("next")
