from Cliente import Cliente 
from Memento import Memento
from ObjetivoChaveJogo import ObjetivoChaveDoJogo

cliente = Cliente()
memento = Memento()
chave_jogo = ObjetivoChaveDoJogo()

cliente.obter_estado()
estado = cliente.restaurar_estado()

memento.set_estado(estado)

chave_jogo.set_memento(memento)
chave_jogo.restaura_estado()

print(chave_jogo.get_estado())