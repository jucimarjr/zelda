from MediatorEx import Mediator

class Evento(Mediator):
    def checarAgenda(self, agenda):
        self.agenda = agenda

    def checarAlarme(self, alarme):
        self.alarme = alarme

    def checarAspersor(self, aspersor):
        self.aspersor = aspersor

    def checarDiaDaSemana(self, diaDaSemana):
        self.diaDaSemana = diaDaSemana

    def fazerCafe(self, cafe):
        self.cafe = cafe

    def ligarDesligarAspersor(self, onAspersor):
        self.onAspersor = onAspersor

    def ligarDesligarAlarme(self, offAspersor):
        self.offAspersor = offAspersor
        
    def checarTemperatura(self, temperatura):
        self.temperatura = temperatura
        
    def checarClima(self, clima):
        self.clima = clima

    def checarChuveiro(self, chuveiro):
        self.chuveiro = chuveiro
