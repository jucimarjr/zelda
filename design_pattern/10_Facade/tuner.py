class Tuner:

    def __init__(self, description, amplifier):
        self._description = description
        self._frequency = None
        self._amplifier = amplifier

    def on(self):
        print (self._description + " on")

    def off(self):
        print (self._description + " off")

    def set_frequency(self, frequency):
        print (self._description + " setting frequency to " + frequency)
        self._frequency = frequency

    def set_am(self):
        print (self._description + " setting AM mode")

    def set_fm(self):
        print (self._description + " setting FM mode")

    def __str__(self):
        return self._description
