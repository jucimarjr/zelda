# -*- coding: utf-8 -*-

class Agenda():
    
    def __init__(self):
        self.lista_contatos = []
        self.cont = 0
    
    def adicionar_pessoa(self, nome, numero):
        self.cont+=1
        self.lista_contatos.append(nome)
        self.lista_contatos.append(numero)


    def exibir_pessoas(self):
        num = 0
        print("\nLista de contatos\n\n")
        
        if len(self.lista_contatos)==0:
            print("Lista vazia!!!\n")

        for i in range(0, len(self.lista_contatos), 2):
            print("{} - Nome: {} | Telefone: {} \n".format(num+1,self.lista_contatos[i],self.lista_contatos[i+1]))
            num+=1
    

    def apagar_pessoa(self, nome, numero):
        for i in range(0, len(self.lista_contatos), 2):
            if nome == self.lista_contatos[i]:
                self.lista_contatos.pop(i+1)
                self.lista_contatos.pop(i)
                self.cont-=1
