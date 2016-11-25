import threading
import time
import copy
from server.py import Userobject

#todo
#give it an object that it will handle such as a file or process
#management of the file or process
#
class Rule(threading.Thread):
    """holds a rule and a callable thread that will run the enforcement
    will put -1 in rulebase if creation of rule is invalid"""
    __rulelock = None
    #number here indicate what parameters are used to determine access control
    #0 = keyposition
    #1 = keyusers
    __rulebase = None
    __keyusers = []
    __otherusers = []
    __currentusers = []
    __keyposition = []
    __numkeyusers = None

    def __init__(self, num, group=None, target=None, name=None, verbose=None, *args, **kargs):
        """args is an array of user names and kargs is an array of position"""
        if (args is None and kargs is None) or num < 1:
            print("Invalid rule.")
            self.__rulebase = -1
        elif args is None:
            self.__rulebase = 0
            self.__numkeyusers = num
            self.__keyposition = copy.deepcopy(kargs)
            #for x in kargs:
            #    self.__keyposition.append(x)
        else:
            self.rulebase = 1
            self.__numkeyusers = num
            self.__keyusers = copy.deepcopy(args)
            #for x in args:
            #    self.__keyusers.append(x)
        self.__rulelock = threading.RLock()
        threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)

    @property
    def checkrulebase(self):
        """return the current rule set"""
        return self.__rulebase

    @property
    def enforcerule(self):
        """see if the current rule is enforced"""
        with self.__rulelock:
            tempnum = self.__numkeyusers
            if self.__keyusers == 1:
                for xname in self.__keyusers:
                    if not xname.getname in self.__currentusers:
                        #rule is broken do something here
                        pass
                    else:
                        tempnum -= 1
                        if tempnum == 0:
                            return True
            else:
                for xpostion in self.__keyposition:
                    if xpostion.getposition in self.__keyposition:
                        tempnum -= 1
                        if tempnum == 0:
                            return True
                if tempnum > 0:
                    #rule is broken do something here
                    pass
    @property
    def removecurrent(self, removee):
        """remove a user from current users"""
        with self.__rulelock:
            for user in self.__currentusers:
                if user.getblueid == removee.getblueid:
                    self.__currentusers.remove(user)
                    break
        return
    @property
    def addcurrent(self, addee):
        """add a user to current users"""
        with self.__rulelock:
            self.__currentusers.append(addee)
        return
    @property
    def kill(self):
        """change the run variable to kill the thread"""
        pass
    @property
    def startcurrent(self, *args):
        """for bulk input of current users, only used when starting the thread"""
        with self.__rulelock:
            for i in args:
                self.__currentusers.append(i)
    @threading
    def run(self):
        """the cold that will run in the back ground"""
        #creat the object the rule is suppose to look after and start it

        while True:
            #DONE lock the resurce __currentusers and check the conditions for the Rule
            #if condition is met, loop back if its broken, close the object and loop back again
            #sleep for x secs between loops
            runbool = self.enforcerule
            if runbool is True:
                #start the object thread
                pass
            else:
                #pause the object thread
                pass
            time.sleep(1)
        #stop the object thread

