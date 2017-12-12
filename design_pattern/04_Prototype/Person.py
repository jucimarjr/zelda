from Prototype import Prototype

class Person(Prototype):
    
    __name = None
    
    def __init__(self, name):
        self.__name = name
        
    def clone(self):
        return Person(self.__name)
        
    def __repr__(self):
        return self.__str__
        
    def __str__(self):
        return "This person is named " + self.__name
