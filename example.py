# CPSC 525
# Andrew Lata, Yue Chen, Justin Berry, Laverne Woroschuk
#
# This is an example python program that demonstrates 
# address and name lookup for nearby bluetooth devices
# in Python

import bluetooth

target_name = "My Phone"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print(bdaddr+"\n")
    print(bluetooth.lookup_name(bdaddr)+"\n")
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"

