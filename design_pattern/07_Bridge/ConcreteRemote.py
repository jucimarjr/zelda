from RemoteControl import *

class ConcreteRemote(RemoteControl):

    _current_station = 0

    def on(self):
        print("A TV está ligada")

    def off(self):
        print("A TV está desligada")

    def next_station(self):
        self._tv.set_channel(current_station + 1)

    def previous_channel(self):
        self._tv.set_channel(current_station - 1)
