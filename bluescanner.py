import threading
import bluetooth
import controlwindow
import time

#takes a lisener for building

class Bluescanner:
    """scan for bluetooth device, and check for differences"""
    __currentuser = []
    __pastuser = []
    __newuser = None
    __outuser = None
    lisener = None

    def __init__(self, a):
        """nothing need to be done here yet"""
        self.__pastuser = bluetooth.discover_devices(duration=8, lookup_names=False, flush_cache=True, lookup_class=False)
        self.lisener = a

    def getchanges(self):
        """get a list of users, and split them into new or outgoing users"""
        self.__newuser = None
        self.__outuser = None
        self.__currentuser = bluetooth.discover_devices(duration=8, lookup_class=False, flush_cache=True)
        newitem = []
        #loop through found users
        for i in self.__currentuser:
            #if new user store it in list
            if i not in self.__pastuser:
                newitem.append(i)
            #if not new just pop it out of old user list
            else:
                self.__pastuser.remove(i)
        self.__newuser = newitem
        self.__outuser = self.__pastuser
        self.__pastuser = self.__currentuser

    @property
    def getnewuser(self):
        """return an array of new users"""
        return self.__newuser

    @property
    def getoutuser(self):
        """return an array of out going users"""
        return self.__outuser

    @property
    def getcurrentuser(self):
        return self.__currentuser

    @threading
    def run(self):
        """check for new users every second"""
        while True:
            self.getchanges()
            if self.__newuser is not None:
                lisener.passadd(self.__newuser)
            if self.__outuser is not None:
                lisener.passdel(self.__outuser)
            time.sleep(1)
