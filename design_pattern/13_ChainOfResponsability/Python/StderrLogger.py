from Logger import Logger

class StderrLogger(Logger):

    def _init_(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Sending to stderr: " + msg)
