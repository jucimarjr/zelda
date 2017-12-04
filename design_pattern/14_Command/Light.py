
class Light:

    def __init__(self, location):
        self._location = location

    def on(self):
        print (self._location + "light is on")

    def off(self):
        print (self._location + "light is off")
