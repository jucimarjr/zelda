from Beverage import Beverage

class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return .89