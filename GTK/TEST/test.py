#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import time
import arrow

class Counter(Gtk.Box):

    conversion={"km":0.001,"km/h":3.6}
    
    def __init__(self,parent,w,h,name,title):
        "docstring"
        print("Counter")
        super(Counter, self).__init__()

        self.set_name(name)
        self.set_spacing(10)
        
        self.Title  = Gtk.Label.new(title)
        self.Title.set_name("Title")
        self.Title.set_size_request(0.3*w,h)
        
        self.Value  = Gtk.Label.new("---")
        self.Value.set_name("Value")
        self.Value.set_size_request(0.5*w,h)
        
        self.Units  = Gtk.Label.new("--")
        self.Units.set_name("Units")
        self.Units.set_size_request(0.1*w,h)

        self.add(self.Title)
        self.add(self.Value)
        self.add(self.Units)
        
        self.set_size_request(w,h)


    ## --------------------------------------------------------------
    ## Description : update la vitesse
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 20-04-2017 14:04:19
    ## --------------------------------------------------------------
    def update (self,value):
        print "update to %s"%value
        
        self.Value.set_label("%s"%value)

        return True        

    ## --------------------------------------------------------------
    ## Description : run counter
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 03-44-2017 09:44:05
    ## --------------------------------------------------------------
    def Run (self,arg):
        while True:
            self.update(arrow.utcnow())
            time.sleep(1)
            

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)

testCounter  = Counter(win,320,100,"testMeter","Something:")
startButton  = Gtk.Button.new_with_label("start")
quitButton   = Gtk.Button.new_with_label("quit")

startButton.connect("clicked", testCounter.Run)
quitButton.connect("clicked", Gtk.main_quit)

grid = Gtk.Grid()
grid.show()
win.add(grid)
grid.attach(testCounter,0,0,1,1)
grid.attach(startButton,0,1,1,1)
grid.attach(quitButton,0,2,1,1)

win.show_all()
Gtk.main()

