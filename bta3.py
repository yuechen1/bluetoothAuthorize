##############
# CPSC 525
# Bluetooth Authorization Application
# (c)2016 - Andrew Lata, Laverne Woroschuk, Justin Berry, Yue Chen
#
# This application is a proof of concept for using Blutooth devices as 
# physical "keys" that can be used in conjunction with other authorization
# mechanisms for providing secure access
##############
#!/usr/bin/env python

from tkinter import *
import bluetooth

# This function queries the nearby Bluetooth devices
def bt_query():
    nearby_devices = bluetooth.discover_devices()

    for bdaddr in nearby_devices:
        print(bdaddr + " ; " + bluetooth.lookup_name(bdaddr) + "\n")

    if nearby_devices is None:
        print("There are no nearby bluetooth devices")


bt_query()
