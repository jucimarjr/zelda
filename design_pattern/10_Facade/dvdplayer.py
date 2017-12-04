class DvdPlayer:

    def __init__(self, description, amplifier):
        self._description = description
        self._amplifier = amplifier
        self._current_track = None
        self._movie = None

    def on(self):
        print (self._description + " on")

    def off(self):
        print (self._description + " off")

    def eject(self):
        print (self._description + " eject")

    def play_movie(self, movie):
        self._movie = movie
        self._current_track = 0
        print (self._description + ' playing "' + self._movie + '"')

    def play_track(self, track):
        if self._movie is None:
            print(self._description + " can't play track " + track +
                  " no dvd inserted")
        else:
            self._current_track = track
            print(self._description + " playing track " + self._current_track +
                  ' of "' + self._movie + '"')

    def stop(self):
        self._current_track = 0
        print (self._description + ' stopped "' + self._movie + '"')

    def pause(self):
        print (self._description + ' paused "' + self._movie + '"')

    def set_two_channel_audio(self):
        print (self._description + " set two channel audio")

    def set_surround_audio(self):
        print (self._description + " set surround audio")

    def __str__(self):
        return self._description
