from Evento import Evento

class Agenda(Evento):
    def checarDiaDaSemana(self, dia):
        self.dia = input("Qual dia da semana? ")

    def fazerCafe(self, cafe):
        print ("Fazendo cafe!")

    def tocarAlarme(self, alarme):
        self.alarme = input("Hora do alarme? ")
        print ("Alarme programado para ", alarme)
