from Command import Command

class LivingRoomOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()
        
