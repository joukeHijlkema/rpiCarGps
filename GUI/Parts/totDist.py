#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 13:53 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import Gtk
from .Counter import Counter

class totDist(Counter):
    def __init__(self,parent,*args,**kw):
        "docstring"
        super(totDist, self).__init__(parent,*args,**kw)

        self.units = "km"
        self.update(0)

