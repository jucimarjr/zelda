from Command import Command

class HottubOffCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.cool()
        self._hottub.off()
        
