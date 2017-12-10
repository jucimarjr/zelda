import PizzaStore

class ChicagoPizzaStore(PizzaStore):

	def create_pizza(item):
		if item == 'cheese'
			return ChicagoStyleCheesePizza()
		elif item == 'veggie':
			return ChicagoStyleVeggiePizza()
		elif item == 'clam':
			return ChicagoStyleClamPizza()
		elif item == 'pereroni':
			return ChicagoStylePepperoniPizza()
		else:
			return None
