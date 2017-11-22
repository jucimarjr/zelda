from CommandFactory import CommandFactory
from BaseCommand import BaseCommand
from CommandEmail import CommandEmail
from CommandPDF import CommandPDF

class Aplicativo():
	__commandFactory = None
	def __init__(self, commandFactory):
		self.__commandFactory = commandFactory

	def buttonEmail_Clicked(self):
		command = self.__commandFactory.create("CommandEmail")
		command.executar()

	def buttonPDF_Clicked(self):
		command = self.__commandFactory.create("CommandPDF")
		command.executar()
