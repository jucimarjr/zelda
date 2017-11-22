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

class EmailLogger(Logger):

    def __init__(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Sending via email: " + msg)

class StderrLogger(Logger):

    def _init_(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Sending to stderr: " + msg)

class StdoutLogger(Logger):

    def _init_(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Writing stdout: " + msg)

def main():
    #x1 = Logger()
    x2 = EmailLogger(None)
    x3 = StderrLogger(None)
    x4 = StdoutLogger(None)
    x2.writeMessage("1");
    x3.writeMessage("2");
    x4.writeMessage("3");

if __name__ == "__main__":
    main()
