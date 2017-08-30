#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - lun. mai 22:33 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from .Counter import Counter

class Altitude(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(Altitude, self).__init__(parent,*args,**kw)

        self.units = "m"
        self.update(0)

