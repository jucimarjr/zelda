import Duck

class RubberDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay)
        self.set_quack_behavior(Squeak)

    def display():
        print("I'm a rubber duckie")
