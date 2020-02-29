#!/bin/bash
sudo rmmod i2c_dev
# sudo rmmod i2c_bcm2708
sleep 1
# sudo modprobe i2c_bcm2708
sudo modprobe i2c_dev
