import threading
import bta.py
import server.py


#main class used to start threads and other classes
#planned classes and their functions
# done  a class to scan for bluetooth devices
#       a class to send message to other threads
#       a class that just hold a rule, can take in an array of current users and give a yes or no answer
#           the class must also be threadable, so it can be run to enforce the rule
#           it will shutdown when the rule is broken or the program is closed
# done  a object process to act as the "server"
# done  a class for user "object"
class mainSystem:
    server = None
    bluescaner = None
    
    def __init__(self):
        """creat all the needed parts"""