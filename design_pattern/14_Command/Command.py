import abc

class Operar(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def operar(self, A, B):
		pass

class Somar(Operar):
	def operar(self, A, B):
		return (A+B)

class Subtrair(Operar):
	def operar(self, A, B):
		return (A-B)

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
