from Evento import Evento

class Aspersor(Evento):
    def __init__(self, aspersor):
        self.aspersor = aspersor

    def OnEvent(self):
        self.med.ligarDesligarAspersor(aspersor)
        if (aspersor == "ligado"):
            print("Aspersor ligado")
        else:
            print("Aspersor desligado")
