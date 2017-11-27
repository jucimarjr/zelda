import Duck

class DecoyDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay)
        self.set_quack_behavior(MuteQuack)

    def display():
        print("I'm a duck Decoy")
