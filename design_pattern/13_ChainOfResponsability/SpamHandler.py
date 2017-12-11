from Handler import Handler

class SpamHandler(Handler):
    def __init__(self, sucessor):
        self.sucessor = sucessor

    def HandleRequest(self, msg):
        print("Executando SpamHandler: " + msg)
