#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:53 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk, Gdk
from .Counter import Counter

class speedMeter(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(speedMeter, self).__init__(parent,*args,**kw)

        self.units = "km/h"
        self.update(277.5)
