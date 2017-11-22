from CommandFactory import CommandFactory
from CommandEmail import CommandEmail
from CommandPDF import CommandPDF

class CommandFactory1(CommandFactory):
	def create(self, nome):
		command = None
		if nome == "CommandEmail":
			print("Do aplicativo 1")
			command = CommandEmail()
		else:
			if nome == "CommandPDF":
				print("Do aplicativo 1")
				command = CommandPDF()
		return command