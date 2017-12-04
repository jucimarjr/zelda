class HomeTheatherFacade:

    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self._amp = amp
        self._tuner = tuner
        self._dvd = dvd
        self._cd = cd
        self._projector = projector
        self._screen = screen
        self._lights = lights
        self._popper = popper

    def watch_movie(self, movie):
        print ("Get ready to watch a movie...")

        self._popper.on()
        self._popper.pop()

        self._lights.dim(10)

        self._screen.down()

        self._projector.on()
        self._projector.wide_screen_mode()

        self._amp.on()
        self._amp.set_dvd(self._dvd)
        self._amp.set_surround_sound()
        self._amp.set_volume(5)

        self._dvd.on()
        self._dvd.play_movie(movie)

    def end_movie(self):
        print ("Shutting movie theater down...")

        self._popper.off()
        self._lights.on()
        self._screen.up()
        self._projector.off()
        self._amp.off()
        self._dvd.stop()
        self._dvd.eject()
        self._dvd.off()

    def listen_to_cd(self, cd_title):
        print ("Get ready for an audiopile experence...")

        self._lights.on()
        self._amp.on()
        self._amp.set_volume(5)
        self._amp.set_stereo_sound()
        self._cd.on()
        self._cd.play(cd_title)

    def end_cd(self):
        print ("Shutting down CD...")
        self._amp.off()
        self._amp.set_cd(self._cd)
        self._cd.eject()
        self._cd.off()

    def listen_to_radio(self, frequency):
        print ("Tuning in the airwaves...")

        self._tuner.on()
        self._tuner.set_frequency(frequency)
        self._amp.on()
        self._amp.set_volume(5)
        self._amp.set_tuner(self._tuner)

    def end_radio(self):
        print ("Shutting down the tuner...")
        self._tuner.off()
        self._amp.off()
