import abc
class Image(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def displayImage(self,input):
		raise NotImplementedError()
