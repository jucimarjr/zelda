from duck import Duck
from fly_with_wings import FlyWithWings
from quack import Quack


class MallardDuck(Duck):

    def __init__(self):
        self.set_fly_behavior(FlyWithWings)
        self.set_quack_behavior(Quack)

    def display():
        print("I'm a real Mallard duck")
