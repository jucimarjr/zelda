import abc
from Computador import Computador

class ComputadorBuilder(metaclass = abc.ABCMeta):
	computador = None

	def getComputador(self):
		return self.computador

	@abc.abstractmethod
	def createComputador(self):
		raise NoImplementedError("A Classe %s não implementa o método createComputador()"%(self.__class__.__name__))
	
	@abc.abstractmethod
	def addPlacaMae(self):
		raise NoImplementedError("A Classe %s não implementa o método addPlacaMae()"%(self.__class__.__name__))
	
	@abc.abstractmethod
	def addHardDisk(self):
		raise NoImplementedError("A Classe %s não implementa o método addHardDisk()"%(self.__class__.__name__))
