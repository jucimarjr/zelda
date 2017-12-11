from Handler import Handler

class ComplainHandler(Handler):
    def __init__(self, sucessor):
        self.sucessor = sucessor

    def HandleRequest(self, msg):
        print("Executando ComplainHandler: " + msg)
