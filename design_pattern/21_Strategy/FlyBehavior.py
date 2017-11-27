import abc

class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly():
        pass
