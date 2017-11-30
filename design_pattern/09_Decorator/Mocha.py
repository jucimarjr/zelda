from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self):
        return .20 + self._beverage.cost()