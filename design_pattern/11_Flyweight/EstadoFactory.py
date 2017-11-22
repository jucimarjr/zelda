from Estado import Estado
class EstadoFactory:

    estados = None

    def __init__(self):
        self.estados = {}#O dicionario contem as instâncias únicas dos Estados

    def get_estado(self, nome):#Captura o objeto estado da classe EstadoFactory

        if (not nome in self.estados):
            estado = Estado(nome)
            self.estados[nome] = estado
        else:
            estado = self.estados[nome]

        return estado #Retorna o objeto Estado da classe EstadoFactory