s1 = "Hello"
s2 = "World!"

person = {
    "name" : "Thomas",
    "surename" : "Funke"
}

class Person :
    name = "name"
    surename = "surename"
    x = 6
    __y = 2 #private

    def __init__(self, 
        name = "default name", 
        surename = "default surename" ) :
        self.name = name
        self.surename = surename

    def toString(self):
        return Person.name, Person.surename

    @staticmethod
    def getSttaticX(): 
        return Person.x


    @classmethod
    def getClsZ(cls): 
        return Person.__y

    @classmethod
    def getClsY(cls): 
        Person.getClsZ()
        return Person.__y

def toString():
    return s1, s2
