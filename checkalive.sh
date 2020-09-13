#!/bin/bash

object="serialRead.py"

#Simple commad for test
#--------------------------------------------#
#pslist=$(ps -aux | grep $object)
#echo $pslist

#Program Start
#--------------------------------------------#
pgnum=$(ps -aux | grep $object | wc -l)
#echo $pgnum
if [[ $pgnum -le 1 ]]; then
    echo "Try to start a new program..."
    sudo python3 /home/pi/ecotech/aurora3000/$object
else
    echo "The program is running..."
fi 
