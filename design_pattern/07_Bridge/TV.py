import abc

class TV(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def on(self):
        pass

    @abc.abstractmethod
    def off(self):
        pass

    @abc.abstractmethod
    def tune_channel(self, channel):
        pass
