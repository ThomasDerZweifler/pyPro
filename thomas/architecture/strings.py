s1 = "Hello"
s2 = "World!"

person = {
    "name" : "Thomas",
    "surename" : "Funke"
}

class Person :
    #name = "name"
    surename = "surename"

    #def __init__(self):
        #self.name = "default"

    def __init__(self, var = "default"):
        self.name = var+ " Thomas"
        surename = var+ " Funke"

    def toString():
        return name, surename

def toString():
    return s1, s2
