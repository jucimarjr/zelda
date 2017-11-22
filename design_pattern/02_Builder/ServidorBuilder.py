from ComputadorBuilder import ComputadorBuilder
from Computador import Computador
from PlacaMae import PlacaMae
from Memoria import Memoria
from CPU import CPU
from HardDisk import HardDisk

class ServidorBuilder(ComputadorBuilder):

	def createComputador(self):
		self.computador = Computador()

	def addPlacaMae(self):
		placaMae = PlacaMae()
		placaMae.add(Memoria())
		placaMae.add(CPU())
		self.computador.add(placaMae)

	def addHardDisk(self):
		self.computador.add(HardDisk())
		self.computador.add(HardDisk())
		self.computador.add(HardDisk())