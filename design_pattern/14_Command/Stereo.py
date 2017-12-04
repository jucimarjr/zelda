
class Stereo:

    def __init__(self, location):
        self._location = location

    def on(self):
        print (self._location + "stereo is on")

    def off(self):
        print (self._location + "stereo is off")

    def set_cd(self):
        print (self._location + "stereo is set for CD input")

    def set_dvd(self):
        print (self._location + "stereo is set for Radio")

    def set_volume(self, volume):
        print (self._location + "stereo volume set to " + str(volume))
