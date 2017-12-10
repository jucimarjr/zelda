class Pizza(object):
	def __init__():			
		self.__name = None
		self.__dough = None
		self.__sauce = None
		self.__toppings = []

	def prepare(self):
		print("Preparing " + self.__name)
		print("Tossing dough...")
		print("Adding sauce...")
		print("Adding toppings: ", *self.__toppings)

	def bake(self):
		print("Bake for  25 min at 350")

	def cut(self):
		print("Cutting the pizza into diagonal slices")

	def box(self):
		print("Place pizza in offical PizzaStore box")

	def get_name(self):
		return self.__name

	def __str__(self):
		return ("---- " + self.__name + " ----\n" +
				self.__dough + "\n" +
				self.__sauce + "\n" +
				*self.__toppings + "\n"
				)
