from Somar import Somar
from Subtrair import Subtrair

class Command():

	def calcular(self, a, b):
		somar = Somar()		
		subtrair = Subtrair()
		print('Soma: ', somar.operar(a, b))
		print('Subtração: ', subtrair.operar(a, b))

if __name__ == "__main__":
	a = int(input())
	b = int(input())
	command = Command()
	command.calcular(a, b)
