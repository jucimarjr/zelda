from duck import Duck
from fly_no_way import FlyNoWay
from mute_quack import MuteQuack

class DecoyDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay)
        self.set_quack_behavior(MuteQuack)

    def display():
        print("I'm a duck Decoy")
