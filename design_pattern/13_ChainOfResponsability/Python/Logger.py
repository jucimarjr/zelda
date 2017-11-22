import abc

class Logger(metaclass=abc.ABCMeta):
    ERR = 3
    NOTICE = 5
    DEBUG = 7

    def __init__(self, mask = None, prox = None):
        self._mask = mask
        self._prox = prox

    def setNext(self, log):
        prox = log
        return prox

    def message (self, msg, priority):
        if(priority <= mask):
            writeMessage(mask)
        if(prox != None):
            prox.message(msg, priority)

    @abc.abstractmethod
    def writeMessage(self, msg):
        pass
