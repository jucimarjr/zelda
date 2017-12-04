
from NoCommand import NoCommand

class RemoteControl:

    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7

    def set_command(self, slot, on_command, of_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = of_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()

    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()

    def __str__(self):
        string_buff = "\n------ Remote Control ------\n"
        for num, command in enumerate(self._on_commands):
            string_buff += ("[slot " + str(num) + "] " +
                             command.__class__.__name__ + "\n")

        return string_buff
