#!/bin/bash
sudo ifconfig ra0 down
sudo make uninstall
sudo make
sudo make install
sudo rmmod rt2860sta
sudo modprobe rt2860sta
sudo ifconfig ra0 up










