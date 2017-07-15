# rpiCarGps
A replacement for the speed indicator of my old van (and it does GPS and a lot more)

# Instalation

## for my screen
	[waveshare 7" touchscreen](http://www.waveshare.com/wiki/7inch_HDMI_LCD)

	add this to end of config.txt

	max_usb_current=1
	hdmi_group=2
	hdmi_mode=87
	hdmi_cvt 1024 600 60 6 0 0 0
	
## SSH

	to allow for ssh acess
	touch /boot/ssh

## dependencies
	sudo apt install navit* mysql-server python-arrow python-gps

## for the database:
	mysql> CREATE DATABASE busGps;
	mysql> SOURCE busGps.sql;
	mysql> CREATE USER 'Jouke'@'localhost' IDENTIFIED BY '!Jouke';
	mysql> GRANT SELECT, INSERT, UPDATE, DELETE ON `busGps`.* TO 'Jouke'@'localhost';


## switch off screen blanking
	add the folowing lines to /etc/xdg/lxsession/LXgfmDE/autostart
	#@xscreensaver -no-splash
	@xset s off
	@xset -dpms
	@xset s noblank


## git repository
`git clone https://github.com/joukeHijlkema/rpiCarGps.git <gpsDir>`

## Maps
- Copy all your maps to /home/pi/Maps/
- Copy <gpsDir>/GPS/myNavit.xml to ~/.navit/navit.xml
