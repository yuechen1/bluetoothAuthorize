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
import tkinter as tk
import bluetooth
#import bluetooth.ble

# This function queries the nearby Bluetooth devices
def bt_query():
    nearby_devices = bluetooth.discover_devices(duration=8,lookup_names=True,flush_cache=True,lookup_class=False)
    for bdAddr,bdName in nearby_devices:
        try:
            print(bdAddr + " ; " + bdName + "\n")
        except UnicodeEncodeError:
            print(bdAddr + " ; " + bdName.encode('utf-8', 'replace') + "\n")

    if len(nearby_devices)==0:
        print("There are no nearby bluetooth devices")
    else:
        print("___________________________________")

class MainWindow(tk.Frame): # MainWindow class defines the contents and behaviors of the window
    def __init__(self,master): # Initialize window with size and title
        tk.Frame.__init__(self,master,width=500,height=400)
        self.master.title("Bluetooth Authorization Demo")
        self.pack_propagate(0)
        self.pack()

    def setControls(self):
        self.startButton = tk.Button(self, text='Scan', command=bt_query)

    def placeWidgets(self):
        self.startButton.pack(fill=tk.X, side=tk.BOTTOM)
        

    def run(self):
        self.setControls()
        self.placeWidgets()
        self.mainloop()


# bt_query()
app = MainWindow(tk.Tk())
app.run()

