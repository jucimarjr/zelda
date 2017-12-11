from Evento import Evento

class Cafeteira(Evento):
    def __init__(self, cafe):
        self.cafe = cafe

    def OnEvent(self):
        if (cafe == "sim"):
            self.fazerCafe()
            print("Fazendo cafe!")
