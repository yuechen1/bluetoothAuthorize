import threading
import bta.py
import server.py


#main class used to start threads and other classes
#planned classes and their functions
# done  a class to scan for bluetooth devices
#       a class to hold the scanner and pass changes to other threads
#           will eventually distinguish between what thread the information will be relivent to
# done  a class that just hold a rule, can take in an array of current users and give a yes or no answer
#           the class must also be threadable, so it can be run to enforce the rule
#           it will pause the object that the rule applys to when the rule is broken
#           it will shutdown the process when
# done  a object process to act as the "server"
# done  a class for user "object"
class mainSystem:
    server = None
    bluescaner = None
    
    def __init__(self):
        """creat all the needed parts"""