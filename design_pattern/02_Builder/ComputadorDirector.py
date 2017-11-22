from ComputadorBuilder import ComputadorBuilder

class ComputadorDirector():
	builder = None

	def __init__(self, builder):
		self.builder = builder

	def buildComputador(self):
		self.builder.createComputador()
		self.builder.addPlacaMae()
		self.builder.addHardDisk()
		return self.builder.getComputador()