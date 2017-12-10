import abc

class PizzaStore(object):
	@abc.abstractmethod
	def create_pizza(item):
		return

	def order_pizza(type):
		pizza = create_pizza(type)
		print("--- Making " + pizza.get_name() + " ---")
		pizza.prepare()
		pizza.bake()
		pizza.cut()
		pizza.box()

		return pizza
