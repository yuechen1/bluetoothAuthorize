
class Server:
    """creats an array of users that can be pulled from"""
    __users = []
    def __init__(self):
        #userobject name,privage, blueid
        self.__users.append(x=Userobject("Person1", "admin", 1))
        self.__users.append(x=Userobject("Person2", "user", 2))
        self.__users.append(x=Userobject("Person3", "admin", 3))
        self.__users.append(x=Userobject("Person4", "user", 4))
    @property
    def getuser(self, b_id):
        """search the bluetooth id of users and return the name and privage level"""
        for i in self.__users:
            if i.getblueid == b_id:
                return i
        return None
    @property
    def someuser(self):
        """returns two admin users for testing"""
        temp = []
        temp.append(self.__users[0])
        temp.append(self.__users[2])
        return temp

class Userobject:
    """used for holding a single user in the database"""
    #name of the user
    #the class/privage level of the user
    #bluetooth id of the user currently just using int but will be changed later
    __name = None
    __position = None
    __blueid = None

    #fill all the needs of the object
    def __init__(self, a, b, c):
        self.name = a
        self.position = b
        self.blueid = c
    @property
    def getposition(self):
        """return the position of user"""
        return self.__position

    @property
    def getname(self):
        """return the name of the user"""
        return self.__name

    @property
    def getblueid(self):
        """return bluetooth id of user"""
        return self.__blueid
