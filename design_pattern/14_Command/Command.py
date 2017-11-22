import abc

class Command(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def operar(self, A, B):
		pass

class Somar(Command):
	def operar(self, A, B):
		return (A+B)

class Subtrair(Command):
	def operar(self, A, B):
		return (A-B)

a = 10
b = 5

somar = Somar()
subtrair = Subtrair()

print('Soma: ', somar.operar(a, b))
print('Subtração: ', subtrair.operar(a, b))
