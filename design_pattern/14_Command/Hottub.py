
class Hottub:

    def __init__(self):
        self._on = on
        self._temperature = 0

    def on(self):
        self._on = True

    def off(self):
        self._off = False

    def bubbles_on(self):
        if self._on is True:
            print ("Hottub is bubbling")

    def jets_on(self):
        if self._on is True:
            print ("Hottub jets are on")

    def jets_off(self):
        if self._on is True:
            print ("Hottub jets are off")

    def set_temperature(self, temperature):
        self._temperature = temperature

    def heat(self):
        self._temperature = 105
        print "Hottub is heating to a steaming a 105 degress"

    def cool(self):
        self._temperature = 98
        print "Hottub is cooling to 98 degress"
