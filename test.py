#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. févr. 18:05 2021
#   - Initial Version 1.0
#  =================================================

args = "truc_1"
match args:
    case "truc":
        print("OK")
    case "machin":
        print("NOK")
    case _:
        print("Default")
        
    
