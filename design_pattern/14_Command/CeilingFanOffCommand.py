from Command import Command

class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.off()
        
