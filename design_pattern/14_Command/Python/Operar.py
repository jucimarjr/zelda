import abc

class Operar(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def operar(self, A, B):
		pass
