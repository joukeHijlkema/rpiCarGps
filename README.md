# rpiCarGps
A replacement for the speed indicator of my old van (and it does GPS and a lot more)

# Instalation

## for my screen
http://www.waveshare.com/wiki/7inch_HDMI_LCD_(B)

add this to end of config.txt

`
max_usb_current=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt 1024 600 60 6 0 0 0
`
## SSH

to allow for ssh acess
`touch /boot/ssh`

## for the database:
`
mysql> CREATE DATABASE busGps;
mysql> SOURCE busGps.sql;
`
