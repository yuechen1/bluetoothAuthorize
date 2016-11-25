import threading
import time
from server import Server
from server import Userobject
from rule import Rule

class Controlwindow:
    """will hold the bluetooth serch class, back ground server and have an array of running rules,
    will take result from the search check it for changes then pass the change to all rule threads.
    will only make the search thread itself, all other threads will be made in main and passed to
    this class to manage."""
    __backserver = None
    __bluescan = None
    __rules = []
    __blueusers = []

    def __init__(self, s, b):
        """get server from main and the bluetooth scanner"""
        self.__backserver = s
        self.__bluescan = b
        #TODO get current users from scanner

    def addrule(self, inputrule):
        """add a rule to the list of rules"""
        self.__rules.append(inputrule)
        inputrule.addcurrent(self.__blueusers)
        inputrule.start()

    def delrule(self, inputrule):
        """shutdown a rule and remove it"""
        inputrule.kill()
        self.__rules.remove(inputrule)

    def passadd(self, *args):
        """pass a new bluetooth user to the relivent thread"""
        for i in self.__rules:
            i.addcurrent(args)

    def passdel(self, *args):
        """delete the bluetooth users from current threads"""
        for i in self.__rules:
            i.removecurrent(args)
