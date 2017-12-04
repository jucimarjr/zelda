class PopcornPopper:

    def __init__(self, description):
        self._description = description

    def on(self):
        print (self._description + " on")

    def off(self):
        print (self._description + " off")

    def pop(self):
        print (self._description + " popping popcorn!")

    def __str__(self):
        return self._description