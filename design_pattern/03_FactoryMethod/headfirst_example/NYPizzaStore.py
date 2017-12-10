import PizzaStore

class NYPizzaStore(PizzaStore):

	def create_pizza(item):
		if item == 'cheese':
			return NYStyleCheesePizza()
		elif item == 'veggie':
			return NYStyleVeggiePizza()
		elif item == 'clam':
			return NYStyleClamPizza()
		elif item == 'pereroni':
			return NYStylePepperoniPizza()
		else:
			return None
