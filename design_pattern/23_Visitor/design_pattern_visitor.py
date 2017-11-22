import abc

class Numero(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def accept(self, visitor):
		 pass

class NumerosConcretos(Numero):
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def accept(self, visitor):
		print (visitor.visit_concrete_element_a(self))

class Visitor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def visit_concrete_element_a(self, NumerosConcretos):
		pass

class SomaVisitor(Visitor):
	def visit_concrete_element_a(self, NumerosConcretos):
		soma = NumerosConcretos.num1 + NumerosConcretos.num2
		return soma		

class SubVisitor(Visitor):
	def visit_concrete_element_a(self, NumerosConcretos):
		sub = NumerosConcretos.num1 - NumerosConcretos.num2
		return sub

def main():
	somaVisitor = SomaVisitor()
	subVisitor = SubVisitor()
	numeroConcreto = NumerosConcretos(2,5)

	numeroConcreto.accept(somaVisitor)
	numeroConcreto.accept(subVisitor)

if __name__ == "__main__":
	main()
