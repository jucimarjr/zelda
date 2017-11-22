from CommandFactory import CommandFactory
from CommandEmail import CommandEmail
from CommandPDF import CommandPDF

class CommandFactory2(CommandFactory):
	def create(self, nome):
		comando = None
		if nome == "CommandEmail":
			print("Do aplicativo 2")
			comando = CommandEmail()
		else:
			if nome == "CommandPDF":
				print("Do aplicativo 2")
				comando = CommandPDF()
		return comando
