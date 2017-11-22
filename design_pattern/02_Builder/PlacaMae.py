from ComponenteComposite import ComponenteComposite

class PlacaMae(ComponenteComposite):
	def getPrecoCusto(self):
		preco = 100
		for c in self.componentes:
			preco += c.getPrecoCusto()
		return preco

	def getPrecoLucroMinimo(self):
		preco = 150
		for c in self.componentes:
			preco += c.getPrecoLucroMinimo()
		return preco

	def getPrecoLucroMaximo(self):
		preco = 200
		for c in self.componentes:
			preco += c.getPrecoLucroMaximo()
		return preco