import threading
from server.py import Userobject

#todo
#give it an object that it will handle such as a file or process
#management of the file or process
#
class Rule:
    """holds a rule and a callable thread that will run the enforcement
    will put -1 in rulebase if creation of rule is invalid"""
    __rulebase = None   #number here indicate what parameters are used to determine access control 
                        #0 = keyposition
                        #1 = keyusers
    __keyusers = []
    __otherusers = []
    __currentusers = []
    __keyposition = []
    __numkeyusers = None
    def __init__(self, num, *args, **kargs):
        """args is an array of user names and kargs is an array of position"""
        if (args == None and kargs == None) or num < 1:
            print("Invalid rule.")
            self.__rulebase = -1
        elif args == None:
            self.__rulebase = 0
            self.__numkeyusers = num
            for x in kargs:
                self.__keyposition.append(x)
        else:
            self.rulebase = 1
            self.__numkeyusers = num
            for x in args:
                self.__keyusers.append(x)
    
    @property
    def checkrulebase(self):
         """return the current rule set"""
         return self.__rulebase
    
    @property
    def enforcerule(self):
        """see if the current rule is enforced"""
        tempnum = self.__numkeyusers
        if self.__keyusers == 1:
            for x in self.__keyusers:
                if not x.getname in self.__currentusers:
                    #rule is broken do something here
                    pass
                else:
                    tempnum -= 1
                    if tempnum == 0:
                        return True
        else:
            for x in self.__keyposition:
                if x.getposition in self.__keyposition:
                    tempnum -= 1
                    if tempnum == 0:
                        return True
            if tempnum > 0:
                #rule is broken do something here
                pass
    
    @threading
    
