# -*- coding: utf-8 -*-

class View():
    def inicio(self):
        print ("Bem vindo a Agenda\n")
        return self.menu()

    def menu(self):
        print ("1 - Para adicionar uma pessoa na agenda")
        print ("2 - Para exibir as pessoas da agenda")
        print ("3 - Para apagar uma pessoa da agenda")
        print ("0 - Sair")

        return int(input("\nDigite a opção: "))

    def get_pessoa(self):
        print ("\nDigite o nome e o telefone a serem inseridos ou apagados")

        nome = input("O nome: ")
        telefone = input("O telefone no formato (xx) xxxxx-xxxx: ")
        return nome, telefone

    def mostrar_resultado(self):
        print ("\nFeito com sucesso!\n")
 


    def finalizar(self):
        print ("Programa finalizado!")