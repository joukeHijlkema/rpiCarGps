# rpiCarGps
A replacement for the speed indicator of my old van (and it does GPS and a lot more)

# Instalation

## for my screen and temp sensor
	[waveshare 7" touchscreen](http://www.waveshare.com/wiki/7inch_HDMI_LCD)

	add this to end of /boot/config.txt

	max_usb_current=1
	hdmi_group=2
	hdmi_mode=87
	hdmi_cvt 1024 600 60 6 0 0 0
	
	dtoverlay=w1-gpio
	
## for the adafruit GPS

	this is for my jessie version look at [adafruit](https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/using-uart-instead-of-usb) for details.
	
	-in /boot/cmdline.txt remove console=serial0,115200
	-sudo systemctl stop serial-getty@ttyS0.service
	-sudo systemctl disable serial-getty@ttyS0.service
	-add enable_uart=1 to the end of /boot/config.txt
	-add GPSD_OPTIONS="/dev/ttyS0 -F /var/run/gpsd.sock" to the end of /etc/default/gpsd
	
## SSH

	to allow for ssh acess
	touch /boot/ssh

## dependencies
	sudo apt install navit* mysql-server gpsd gpsd-clients git
	sudo -H pip3 install gps3 mysql-connector==2.1.6 arrow
	
## git repository but you probably already have it if you're reading this

``` script
git clone https://github.com/joukeHijlkema/rpiCarGps.git <gpsDir>
```

## for the database (the file lives in th DB directory)
	mysql> CREATE DATABASE busGps;
	mysql> USE busGps;
	mysql> SOURCE busGps.sql;
	mysql> CREATE USER 'Jouke'@'localhost' IDENTIFIED BY '!Jouke';
	mysql> GRANT SELECT, INSERT, UPDATE, DELETE ON `busGps`.* TO 'Jouke'@'localhost';


## switch off screen blanking
	change two settings in /etc/kbd/config 
	BLANK_TIME=0
	POWERDOWN_TIME=0

	add the folowing lines to /etc/xdg/lxsession/LXDE/autostart and /etc/xdg/lxsession/LXDE-pi/autostart
	#@xscreensaver -no-splash
	@xset s off
	@xset -dpms
	@xset s noblank

## Maps
- Copy all your maps to /home/pi/Maps/
- Copy or link <gpsDir>/GPS/myNavit.xml to ~/.navit/navit.xml

## to auto start
put a file called rpiGps.desktop in ~/.config/autostart containing :


``` script
[Desktop Entry]
Type=Application
Exec=/home/pi/Projects/rpiCarGps/run.py
Hidden=false
X-GNOME-Autostart-enabled=true
Name=rpiCarGps
Comment=rpiCarGps
Terminal=false
Icon=/home/pi/Projects/rpiCarGps/GUI/Icons/compass.png
Path=/home/pi/Projects/rpiCarGps/
StartupNotify=false
```

## Python
I switched to glade for the GUI. The catalog file is in GLADE/CATALOG
