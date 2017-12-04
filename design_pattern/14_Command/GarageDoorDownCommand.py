from Command import Command

class GarageDoorDownCommand(Command):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.down()
