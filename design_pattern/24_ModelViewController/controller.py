# -*- coding: utf-8 -*-


from model.agenda import Agenda
from viewTerminal.view import View


class CtrlAgenda():
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 0:
            resultado = self.operacao(opcao)
            self.view.mostrar_resultado()
            opcao = self.view.menu()

        self.view.finalizar()

    def operacao(self, opcao):

        if opcao == 1:
            nome, numero = self.view.get_pessoa()
            return self.model.adicionar_pessoa(nome, numero)
        elif opcao == 2:
            return self.model.exibir_pessoas()
        else:
            nome, numero = self.view.get_pessoa()
            return self.model.apagar_pessoa(nome, numero)

    def __init__(self):
        self.model = Agenda()
        self.view = View()


if __name__ == "__main__":
    main = CtrlAgenda()
    main.inicio()

