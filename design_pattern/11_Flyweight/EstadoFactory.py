from Estado import Estado
class EstadoFactory:

    __estados = None

    def __init__(self):
        self.__estados = {}#O dicionario contem as instâncias únicas dos Estados

    def get_estado(self, nome):#Captura o objeto estado da classe EstadoFactory

        if (not nome in self.__estados):
            estado = Estado(nome)
            self.__estados[nome] = estado
        else:
            estado = self.__estados[nome]

        return estado #Retorna o objeto Estado da classe EstadoFactory

    def get_estados(self):
        return self.__estados
