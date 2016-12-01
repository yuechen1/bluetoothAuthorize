import threading
import bluescanner
import server
import controlwindow
import rule


#main class used to start threads and other classes
#planned classes and their functions
# DONE  a class to scan for bluetooth devices
# DONE      have a function that will return a list of bluetooth device
# DONE      if possible return only the changes in bluetooth device
# Done  a class to pass changes to other threads
#           will eventually distinguish between what thread the information will be relivent to
# DONE  a class that just hold a rule, can take in an array of current users and give a yes or no answer
# DONE      the class must also be threadable, so it can be run to enforce the rule
# TODO      it will pause the object that the rule applys to when the rule is broken
# TODO      it will shutdown the process when killed
# done  a object process to act as the "server"
# done  a class for user "object"
class mainSystem:
    backserver = None
    scaner = None
    control = None

    def __init__(self):
        """creat all the needed parts"""
        backserver = server.Server()#start the server
        control = controlwindow.Controlwindow(backserver)#create the lisener
        scanner = bluescanner.Bluescanner(control)#create the scanner
        scanner.run
        #num = number of people needed
        #group must be None
        #target must be None
        #name must be None
        #verbose must be None
        #*args array of users
        #**kargs arrary of positions
        newrule = rule.Rule(2, None, None, None, None, {backserver.someuser}, None)
        control.addrule(newrule, scanner.getcurrentuser)
        