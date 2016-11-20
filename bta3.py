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
def bt_query_device():
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

#def bt_query_le():

class MainWindow(tk.Frame): # MainWindow class defines the contents and behaviors of the window
    def __init__(self,master): # Initialize window with size and title
        tk.Frame.__init__(self,master,width=500,height=400)
        self.master.title("Bluetooth Authorization Demo")
        self.pack_propagate(0)
        self.pack()

    def setControls(self):
        self.startButton = tk.Button(self, text='Scan', command=bt_query_device)
        self.authList = tk.Listbox(self, height=5, selectmode=SINGLE)
        self.addAddress = StringVar(self, value="-- Address --")
        self.addButton = tk.Button(self, text="Add Address", command=self.addDevice)
        self.inputAddAuth = tk.Entry(self, justify=CENTER, textvariable=self.addAddress)
        self.removeButton = tk.Button(self,text="Remove",command=self.removeDevice)
        self.authLabel = tk.Message(self,anchor=CENTER,justify=CENTER,pady=20,text="NOT AUTHORIZED")

    def placeWidgets(self):
        self.startButton.pack(fill=tk.X, side=tk.BOTTOM)
        self.removeButton.pack(fill=tk.X, side=tk.BOTTOM)
        self.authList.pack(fill=tk.X, anchor=N, side=tk.BOTTOM)
        self.addButton.pack(fill=tk.X, side=tk.BOTTOM)
        self.inputAddAuth.pack(fill=tk.X, side=tk.BOTTOM)
        self.authLabel.pack(fill=tk.X, side=tk.TOP)

    def addDevice(self):
        newAddress = self.inputAddAuth.get()
        self.authList.insert(END,newAddress)

    def removeDevice(self):
        self.authList.delete(self.authList.curselection())

    def authLoop(self):
        authorized = False
        nearbyNum = 0
        while(True):
            nearbyNum = 0
            nearby_devices = bluetooth.discover_devices(duration=8,lookup_names=False,flush_cache=True,lookup_class=False)
            for bdAddr in nearby_devices:
                i = 0
                while(i < self.authList.size()):
                    if (bdAddr==self.authList.get(i)):
                        nearbyNum=nearbyNum+1
                    i=i+1
            if(nearbyNum == self.authList.size()):
                self.authLabel['text']="Authorized"
#               self.authLabel['color']
            

    def run(self):
        self.setControls()
        self.placeWidgets()
        self.mainloop()


# bt_query()
app = MainWindow(tk.Tk())
app.run()

