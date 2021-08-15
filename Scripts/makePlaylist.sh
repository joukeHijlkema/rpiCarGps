#!/bin/bash
echo "this needs be be run on the rpi. No ssh!"
mpc lsplaylists
mpc clear
mpc ls | mpc add
mpc save All
