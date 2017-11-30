from Beverage import Beverage
from CondimentDecorator import CondimentDecorator

class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return .10 + self._beverage.cost()