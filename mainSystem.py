import threading
import bta.py

#main class used to start threads and other classes
#planned classes and their functions
#       a class to scan for bluetooth devices
#       a class to send message to other threads
#       a class to manage the decision process
# done  a background process to act as the "server"
# done  a class for user "object"
class mainSystem:
    server = None
    bluescaner = None
    
    def __init__(self):
