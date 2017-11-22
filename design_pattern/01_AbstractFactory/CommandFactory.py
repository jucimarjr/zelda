import abc

class CommandFactory(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def create(self, nome):
		raise NoImplementedError("A Classe %s não implementa o método create(self, nome)"%(self.__class__.__name__))