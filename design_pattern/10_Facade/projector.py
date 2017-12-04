class Projector:

    def __init__(self, description, dvd_player):
        self._description = description
        self._dvd_player = dvd_player

    def on(self):
        print (self._description + " on")

    def off(self):
        print (self._description + " off")

    def wide_screen_mode(self):
        print (self._description + " in widescreen mode (16x9 aspect ratio)")

    def tv_move(self):
        print (self._description + " in tv mode (4x3 aspect ratio)")

    def __str__(self):
        return self._description
