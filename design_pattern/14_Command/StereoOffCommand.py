from Command import Command

class StereoOffCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()
        
