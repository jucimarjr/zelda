from Logger import Logger

class EmailLogger(Logger):

    def __init__(self, mask):
        self.mask = mask

    def writeMessage(self, msg):
        print("Sending via email: " + msg)
