from abc import ABCMeta, abstractmethod

class Beverage:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass