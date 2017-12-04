
class GarageDoor:

    def __init__(self, location):
        self._location = location

    def up(self):
        print (self._location + "garage Door is Up")

    def down(self):
        print (self._location + "garage Door is Down")

    def stop(self):
        print (self._location + "garage Door is Stopped")

    def light_on(self):
        print (self._location + "garage light is on")

    def light_off(self):
        print (self._location + "garage light is off")
