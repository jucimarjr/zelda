class TheaterLights:

    def __init__(self, description):
        self._description = description

    def on(self):
        print (self._description + " on")

    def off(self):
        print (self._description + " off")

    def dim(self, level):
        print (self._description + " dimming to " + str(level) + " %")

    def __str__(self):
        return self._description