import abc
from Componente import Componente

class ComponenteComposite(Componente, metaclass = abc.ABCMeta):
	componentes = None
	def __init__(self):
		self.componentes = []

	def add(self, componente):
		self.componentes.append(componente)