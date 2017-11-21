import abc

class Componente:
	@abc.abstractmethod
	def getPrecoCusto(self):
		return

	@abc.abstractmethod
	def getPrecoLucroMinimo(self):
		return

	@abc.abstractmethod
	def getPrecoLucroMaximo(self):
		return


class ComponenteComposite(Componente):
	_componentes = []

	def __init__(self):
		self._componentes = []

	def add(self,c):
		self._componentes.append(c)

class Computador(ComponenteComposite):
	
	def getPrecoCusto(self):
		print("Calculando Preco de custo da composição:")
		preco = 0
		for c in self._componentes :
			preco += c.getPrecoCusto()
		return preco

	def getPrecoLucroMinimo(self):
		print("Calculando Preco de lucro mínimo da composição:")
		preco = 0
		for c in self._componentes :
			preco += c.getPrecoLucroMinimo()
		return preco

	def getPrecoLucroMaximo(self):
		print("Calculando Preco de lucro maximo da composição:")
		preco = 0
		for c in self._componentes :
			preco += c.getPrecoLucroMaximo()
		return preco

	def getComputadorIterator(self):
		return ComputadorIterator(self)

class ComputadorIterator:
	__computador = Computador()
	__current = 0
	__steps = 0

	def __init__(self, c):
		self.__computador = c

	def proximoComponente(self):
		self.__current += 1
		self.__steps = 0
		r = self.getComponente(self.__computador)
		if r == None :
			self.__current -= 1
		return r

	def ComponenteAnterior(self):
		self.__current -= 1
		self.__steps = 0
		r = self.getComponente(self.__computador)
		if r == None :
			self.__current += 1
		return r
	def getComponente(self, cl):
		retorno = None
		for c in cl._componentes :
			self.__steps += 1
			if type(c) in [Computador, PlacaMae] :
				if self.__steps == self.__current :
					retorno = c
					break
				else:
					cll = self.getComponente(c)
					if cll == None and self.__steps == self.__current :
						return None
					elif cll != None and self.__steps == self.__current :
						return cll
			else:
				if self.__steps == self.__current :
					retorno = c
					break

		return retorno


class CPU(Componente):

	def getPrecoCusto(self):
		return 300

	def getPrecoLucroMinimo(self):
		return 400

	def getPrecoLucroMaximo(self):
		return 600


class HardDisk(Componente):

	def getPrecoCusto(self):
		return 100

	def getPrecoLucroMinimo(self):
		return 120

	def getPrecoLucroMaximo(self):
		return 200


class Memoria(Componente):

	def getPrecoCusto(self):
		return 50

	def getPrecoLucroMinimo(self):
		return 60

	def getPrecoLucroMaximo(self):
		return 120


class PlacaMae(ComponenteComposite):
	
	def getPrecoCusto(self):
		print("Calculando Preco de custo da composição:")
		preco = 100
		for c in self._componentes :
			preco += c.getPrecoCusto()
		return preco

	def getPrecoLucroMinimo(self):
		print("Calculando Preco de lucro mínimo da composição:")
		preco = 150
		for c in self._componentes :
			preco += c.getPrecoLucroMinimo()
		return preco

	def getPrecoLucroMaximo(self):
		print("Calculando Preco de lucro maximo da composição:")
		preco = 200
		for c in self._componentes :
			preco += c.getPrecoLucroMaximo()
		return preco

c1 = Computador()

placaMae = PlacaMae()

memoria1 = Memoria()
memoria2 = Memoria()
cpu = CPU()

placaMae.add(memoria1)
placaMae.add(memoria2)
placaMae.add(cpu)
c1.add(placaMae)

hd1 = HardDisk()
hd2 = HardDisk()

c1.add(hd1)
c1.add(hd2)

print("Listando os componentes do computador:")

i = c1.getComputadorIterator()
clista = i.proximoComponente()
while(clista != None):
	nome = str(type(clista))
	preco = str(clista.getPrecoCusto())
	print("Componente " + nome + " Preco Custo: " + preco)
	clista = i.proximoComponente()