class Memento():
    __estado_jogo = ""

    def get_estado(self):
        return self.__estado_jogo

    def set_estado(self,estado_jogo):
        self.__estado_jogo = estado_jogo
