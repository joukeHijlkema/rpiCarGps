#!/bin/bash
sudo cp /home/pi/rpiCarGps/Scripts/carGps.service /etc/systemd/system/.
sudo cp /home/pi/rpiCarGps/Scripts/shutdown.service /etc/systemd/system/.
sudo cp /home/pi/rpiCarGps/Scripts/volumeControl.service /etc/systemd/system/.
sudo cp /home/pi/rpiCarGps/Scripts/audioLink.service /etc/systemd/system/.

sudo systemctl daemon-reload
