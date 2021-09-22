#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. août 15:05 2021
#   - Initial Version 1.0
#  =================================================
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk, GdkPixbuf, Gio, GLib, Vte

import os

class Terminal(Gtk.Box):
    def __init__ (self):
        super(Terminal, self).__init__()
        self.terminal_box = Gtk.HBox()
        self.terminal     = Vte.Terminal()
        self.terminal.spawn_sync(Vte.PtyFlags.DEFAULT, os.getcwd(), 
                                 ["/bin/bash"], [], GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None,)
        self.terminal_box.pack_start(self.terminal, True, True, 0)
        self.scrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.VERTICAL,
                                       adjustment = Gtk.Scrollable.get_vadjustment(self.terminal))
        self.terminal_box.pack_start(self.scrollbar,False, False, 0)
        self.pack_start(self.terminal_box,True,True,0)
        self.show_all()
        self.startup_cmds=["PS1='Termaxx@$PWD $: '\n","clear\n"]

        self.menu = Gtk.Menu()
    
        self.menuitem1 = Gtk.MenuItem.new_with_label("Copy")
        self.menuitem1.connect("activate",self.copy)
        self.menuitem1.show()

        self.menuitem2 = Gtk.MenuItem.new_with_label("Paste")
        self.menuitem2.connect("activate",self.paste)
        self.menuitem2.show()

        self.menuitem3 = Gtk.MenuItem.new_with_label("Clear")
        self.menuitem3.connect("activate",self.clear)
        self.menuitem3.show()

        self.menu.append(self.menuitem1)
        self.menu.append(self.menuitem2)
        self.menu.append(self.menuitem3)
    

        for i in self.startup_cmds:
            self.run_command(i)
            self.connect_object("event", self.button_press, self.menu)

    def run_command(self,cmd):
        self.terminal.feed_child_binary(bytes(cmd,'utf8'))

    def button_press(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_RELEASE:
            x,button = event.get_button()
            if button == Gdk.BUTTON_SECONDARY:
                widget.popup(None,None, None, None, button, Gdk.CURRENT_TIME) 

    def copy(self,widget):
        self.terminal.copy_primary()

    def paste(self,widget):
        self.terminal.paste_primary()

    def clear(self,widget):
        self.run_command("clear\n")                 

if __name__ == '__main__':

    win = Gtk.Window()
    win.set_default_size(600, 300)

    term = Terminal()
    win.add(term)

    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
