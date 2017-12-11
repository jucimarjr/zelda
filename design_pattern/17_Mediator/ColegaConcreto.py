from Evento import Evento

class ColegaConcreto():

    def alarmeEvento(self,despertador):
        evento = Evento()
        if(despertador == "ligado"):
            evento.fazerCafe("sim")
            print("Sem preparo de café!")
        else:
            evento.fazerCafe("nao")
            print("Fazendo café!")

    def banhoEvento(self, banho):
        evento = Evento()
        if (banho == "sim"):
            evento.ligarDesligarAspersor(banho)
            print("Aspersor desligará após 15 minutos!")
        else:
            evento.ligarDesligarAspersor(banho)
            print("Aspersor delisgado!")

        
    def diaDoLixo(self, lixo):
        evento = Evento()
        self.lixo = lixo
        if(lixo == "sim"):
            alarme = input ("Hora do alarme: ")
            evento.ligarDesligarAlarme(alarme)
            print("Alarme programada para às %s horas" % alarme)

    def fimDeSemana (self, fds):
        evento = Evento()
        self.fds = fds
        if (fds == "sim"):
            evento.fazerCafe(fds)
            print ("Sem preparo de café!")
        else:
            evento.fazerCafe(fds)
            print("Fazendo café!")
