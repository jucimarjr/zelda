from Beverage import Beverage

class Decaf(Beverage):

    def __init__(self):
        self._description = "Decaf Coffee"

    def cost(self):
        return 1.05