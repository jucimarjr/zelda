from Command import Command

class LightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()
        
