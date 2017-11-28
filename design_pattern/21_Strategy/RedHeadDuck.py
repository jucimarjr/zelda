from Duck import Duck
from FlyWithWings import FlyWithWings
from Quack import Quack

class RedHeadDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyWithWings)
        self.set_quack_behavior(Quack)

    def display():
        print("I'm a real Red Headed duck")
