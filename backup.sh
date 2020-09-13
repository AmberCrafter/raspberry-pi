#!/bin/bash

# show disk and device condition
# lsblk
# sudo fdisk -l

# mount new usb
echo "Mounting usb"
sudo mount /dev/sda1 /mnt/usb

# copy data
echo "Copy data, please wait..."
sudo cp -r /home/pi/ecotech/aurora3000/data /mnt/usb/
echo "Copy finished."

# Unmount usb
echo "Unmount usb, please wait..."
sudo umount /dev/sda1
