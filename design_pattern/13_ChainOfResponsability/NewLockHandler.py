from Handler import Handler

class NewLockHandler(Handler):
    def __init__(self,sucessor):
        self.sucessor = sucessor

    def HandleRequest(self, msg):
        print("Executando NewLockHandler: " + msg)

