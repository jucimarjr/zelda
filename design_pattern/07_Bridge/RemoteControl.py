class RemoteControl:

    def __init__(self, tv):
        self._tv = tv

    def on(self):
        self._tv.on()

    def off(self):
        self._tv.off()

    def set_channel(self, channel):
        self._tv.tune_channel(channel)
