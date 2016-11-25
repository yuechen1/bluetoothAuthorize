import threading
import bta
import server


#main class used to start threads and other classes
#planned classes and their functions
# DONE  a class to scan for bluetooth devices
# DONE      have a function that will return a list of bluetooth device
# DONE      if possible return only the changes in bluetooth device
#       a class to hold the scanner and pass changes to other threads
#           will eventually distinguish between what thread the information will be relivent to
# DONE  a class that just hold a rule, can take in an array of current users and give a yes or no answer
# DONE      the class must also be threadable, so it can be run to enforce the rule
# TODO      it will pause the object that the rule applys to when the rule is broken
# TODO      it will shutdown the process when
# done  a object process to act as the "server"
# done  a class for user "object"
class mainSystem:
    server = None
    bluescaner = None
    
    def __init__(self):
        """creat all the needed parts"""