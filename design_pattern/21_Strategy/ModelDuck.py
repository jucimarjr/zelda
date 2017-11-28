from Duck import Duck
from FlyNoWay import FlyNoWay
from Quack import Quack

class ModelDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay)
        self.set_quack_behavior(Quack)

    def display():
        print("I'm a model duck")
