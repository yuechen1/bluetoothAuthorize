import bluetooth

class Bluescanner:
    """scan for bluetooth device, and check for differences"""
    __currentuser = []
    __pastuser = []
    __devices = None
    __newuser = None
    __outuser = None

    def __init__(self):
        """nothing need to be done here yet"""
        self.__pastuser = bluetooth.discover_devices(duration=8, lookup_names=False, flush_cache=True, lookup_class=False)


    def getchanges(self):
        """get a list of users, and split them into new or outgoing users"""
        self.__devices = bluetooth.discover_devices(duration=8, lookup_class=False, flush_cache=True)
        newitem = []
        for i in self.__currentuser:
            if i not in self.__pastuser:
                newitem.append(i)
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
