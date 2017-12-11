from Handler import Handler

class FanHandler(Handler):
    def __init__(self, sucessor):
        self.sucessor = sucessor

    def HandleRequest(self, msg):
        print("Executando HandleRequest: " + msg)
