from abc import ABCMeta, abstractmethod
from Beverage import Beverage

class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_description(self):
        pass