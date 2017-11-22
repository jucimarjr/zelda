from Logger import Logger

class StdoutLogger(Logger):

    def _init_(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Writing stdout: " + msg)
