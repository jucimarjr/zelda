from Memento import Memento

class ObjetivoChaveDoJogo():
    __estado_jogo = ""
    memento = Memento()
    
    def set_memento(self, memento):
        self.memento = memento

    def criar_memento(self):
        m = Memento()
        return m

    def restaura_estado(self):
        self.__estado_jogo = self.memento.get_estado()
    
    def get_estado(self):
        return self.__estado_jogo
