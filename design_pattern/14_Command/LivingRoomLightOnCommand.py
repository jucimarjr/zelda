from Command import Command

class LivingRoomOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()
        
