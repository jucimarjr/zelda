from Prototype import Prototype

class Dog(Prototype):
    
    __sound = None
    
    def __init__(self, sounxd):
        self.__sound = sound
        
    def clone(self):
        return Dog(self.__sound)

    def __repr__(self):
        return self.__str__
        
    def __str__(self):
        return "This dog says " + self.__sound
