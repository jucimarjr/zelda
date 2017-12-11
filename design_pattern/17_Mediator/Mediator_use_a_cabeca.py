from ColegaConcreto import ColegaConcreto    
from Agenda import Agenda
from Cafeteira import Cafeteira
from Aspersor import Aspersor
from MediatorEx import Mediator
from Evento import Evento


colega = ColegaConcreto()

despertador = input("Despertador (ligado ou desligado): ")
colega.alarmeEvento(despertador)

banho  = input("Banho programada? (sim ou nao): ")
colega.banhoEvento(banho)

dia_lixo = input("Dia do lixo? (sim ou nao): ")
colega.diaDoLixo(dia_lixo)

fim_de_semana = input("Fim de semana? (sim ou nao): ")
colega.fimDeSemana(fim_de_semana)
