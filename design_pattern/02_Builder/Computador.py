from ComponenteComposite import ComponenteComposite

class Computador(ComponenteComposite):	
	def getPrecoCusto(self):
		preco = 0
		for c in self.componentes:
			preco += c.getPrecoCusto()
		return preco

	def getPrecoLucroMinimo(self):
		preco = 0
		for c in self.componentes:
			preco += c.getPrecoLucroMinimo()
		return preco

	def getPrecoLucroMaximo(self):
		preco = 0
		for c in self.componentes:
			preco += c.getPrecoLucroMaximo()
		return preco