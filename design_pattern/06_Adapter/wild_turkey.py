# *
# * Implementação concreta de um turkey.
# *

class wild_turkey(object):
    duck_interface = property()

    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")
