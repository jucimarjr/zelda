from Aplicativo import Aplicativo
from CommandFactory1 import CommandFactory1
from CommandFactory2 import CommandFactory2

class AbstractFactory():
	def __init__(self):
		aplicativo1 = Aplicativo(CommandFactory1())
		aplicativo2 = Aplicativo(CommandFactory2())
		
		aplicativo1.buttonEmail_Clicked()
		aplicativo1.buttonPDF_Clicked()

		aplicativo2.buttonEmail_Clicked()
		aplicativo2.buttonPDF_Clicked()