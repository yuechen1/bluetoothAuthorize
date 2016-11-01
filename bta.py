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

import Tkinter as tk
import bluetooth

class MainWindow(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master,width=500,height=400)

        # Sets the title
        self.master.title("Bluetooth Authorization Engine")

        # Allows the size specification to take effect
        self.pack_propagate(0)

        # Flexible pack layout manager
        self.pack()

        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,
                                      self.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        self.greeting_var.set('hello')
 
        # The recipient text entry control and its StringVar
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,
                                  textvariable=self.recipient_var)
        self.recipient_var.set('world')
 
        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)
 
        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)
 
    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. '''
        print('%s, %s!' % (self.greeting_var.get().title(),
                           self.recipient_var.get()))
    def run(self):
        ''' Run the app '''
        self.mainloop()
 
app = MainWindow(tk.Tk())
app.run()
