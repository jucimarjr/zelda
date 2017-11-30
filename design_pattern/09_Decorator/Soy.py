from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Soy"

    def cost(self):
        return .15 + self._beverage.cost()