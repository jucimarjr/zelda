from abc import ABCMeta, abstractmethod

class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement:
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass

