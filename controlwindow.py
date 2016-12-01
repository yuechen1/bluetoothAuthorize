import threading
import time
import server
import rule

class Controlwindow:
    """will take changes from search then pass the change to all rule threads.
    all rule threads will be made in main and passed to this class to manage.
    This is the only class that make use of the server, it will search the 
    server for the registered users that shows up in changes then pass them to
    threads"""
    backserver = None
    __rules = []

    def __init__(self, s):
        """get server from main"""
        self.backserver = s

    def addrule(self, inputrule, *args):
        """add a rule to the list of rules"""
        temp = []
        for i in args:
            checkuser = backserver.getuser(i)
            if checkuser is not None:
                temp.append(checkuser)
        self.__rules.append(inputrule)
        inputrule.startcurrent(temp)
        inputrule.start()

    def delrule(self, inputrule):
        """shutdown a rule and remove it"""
        inputrule.kill()
        self.__rules.remove(inputrule)

    def passadd(self, *args):
        """pass a new bluetooth user to the relivent thread"""
        temp = []
        for i in args:
            checkuser = backserver.getuser(i)
            if checkuser is not None:
                temp.append(checkuser)
        for i in self.__rules:
            i.addcurrent(temp)

    def passdel(self, *args):
        """delete the bluetooth users from current threads"""
        temp = []
        for i in args:
            checkuser = backserver.getuser(i)
            if checkuser is not None:
                temp.append(checkuser)
        for i in self.__rules:
            i.removecurrent(args)
