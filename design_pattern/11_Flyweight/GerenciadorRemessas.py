from EstadoFactory import EstadoFactory
from Remessa import Remessa

class GerenciadorRemessas:

    __remessas = None

    def __init__(self):
        self.__remessas = []
        self.__estado_factory = EstadoFactory()

    def gerar_remessa(self, e):
        estado = self.__estado_factory.get_estado(e)
        self.__remessas.append(estado)

    def mostrar_remessas(self):#verificação
        for remessa in self.__remessas:
            print(remessa.get_nome())

    def mostrar_estado_factory(self):#verificação
        print(self.__estado_factory.get_estados())
