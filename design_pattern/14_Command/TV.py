
class TV:

    def __init__(self, location):
        self._location = location
        self._channel = 0

    def on(self):
        print "TV is on"

    def off(self):
        print "TV is off"

    def set_input_channel(self):
        self._channel = 3
        print "Channel is set for VCR"
