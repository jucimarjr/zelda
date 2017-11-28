import abc

class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack():
        pass
