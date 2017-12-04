
class CeilingFan:
    HIGH = 2
    MEDIUM = 1
    LOW = 0

    def __init__(self, location):
        self._location = location
        self._level = 0

    def high(self):
        self._level = CeilingFan.HIGH
        print (self._location + "ceiling fan is on high")

    def medium(self):
        self._level = CeilingFan.MEDIUM
        print (self._location + "ceiling fan is on medium")

    def low(self):
        self._level = CeilingFan.LOW
        print (self._location + "ceiling fan is on low")

    def off(self):
        self._level = 0
        print (self._location + "ceiling fan is off")

    def get_speed():
        return self._level
