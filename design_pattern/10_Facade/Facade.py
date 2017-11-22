class Cachorro:
    def falar(self):
        print ("AU! AU!")

class Gato:
    def falar(self):
        print ("MIAU!")

class Chamar:
    def __init__(self):
        self.cachorro = Cachorro()
        self.gato = Gato()
    def chamar(self):
        self.cachorro.falar()
        self.gato.falar()

if __name__ == '__main__':
    facade = Chamar()
    facade.chamar()
