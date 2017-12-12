# *
# * Uma subclasse de duck_interface,
# * a MallardDuck
# *

class mallard_duck(object):
    duck_interface = property()

    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")
