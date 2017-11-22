import abc

class Componente(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def getPrecoCusto(self):
		raise NoImplementedError("A Classe %s não implementa o método getPrecoCusto()"%(self.__class__.__name__))
	
	@abc.abstractmethod
	def getPrecoLucroMinimo(self):
		raise NoImplementedError("A Classe %s não implementa o método getPrecoLucroMinimo()"%(self.__class__.__name__))
	
	@abc.abstractmethod
	def getPrecoLucroMaximo(self):
		raise NoImplementedError("A Classe %s não implementa o método getPrecoLucroMaximo()"%(self.__class__.__name__))
