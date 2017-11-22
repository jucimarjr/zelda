from ServidorBuilder import ServidorBuilder
from ComputadorDirector import ComputadorDirector
from Computador import Computador

class Aplicativo():
	builder = None
	def __init__(self):
		builder = ServidorBuilder()
		director = ComputadorDirector(builder)
		computador = director.buildComputador()
		
		computador.getPrecoLucroMaximo()