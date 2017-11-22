import abc

class BaseCommand(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def executar(self):
		raise NotImplementedError("Classe %s não implementa o método executar()"%(self.__class__.__name__))