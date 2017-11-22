from EstadoFactory import EstadoFactory
from Remessa import Remessa

class GerenciadorRemessas:

    remessas = None

    def __init__(self):
        self.remessas = []
        self.estado_factory = EstadoFactory()

    def gerar_remessa(self, e):
        estado = self.estado_factory.get_estado(e)
        self.remessas.append(estado)

    def mostrar_remessas(self):#verificação
        for remessa in self.remessas:
            print(remessa.get_nome())

    def mostrar_estado_factory(self):#verificação
        print(self.estado_factory.estados)

