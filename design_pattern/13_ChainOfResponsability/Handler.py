import abc

class Handler(metaclass=abc.ABCMeta):
    def __init__(self, sucessor):
        self.sucessor = sucessor

    @abc.abstractmethod
    def HandleRequest(self, msg):
        pass
