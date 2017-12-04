from Command import Command

class GarageDoorUpCommand(Command):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.up()
        
