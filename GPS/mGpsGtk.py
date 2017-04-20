#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. avril 17:29 2017
#   - Initial Version 1.0
#  =================================================
from gi.repository import GObject
import gps

class myGps(GObject.GObject):
    def __init__(self, args):
        "docstring"
        
