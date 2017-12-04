from Command import Command

class HottubOnCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.on()
        self._hottub.self()
        self._hottub.bubbles_on()
