from .headfirst_example import NYPizzaStore


def main():
	ny_store = NYPizzaStore()
	chicagoStore = ChicagoPizzaStore()

	pizza = ny_store.orderPizza("cheese")
	print("Ethan ordered a " + pizza.get_name() + "\n")

	pizza = chicagoStore.orderPizza("cheese")
	print("Joel ordered a " + pizza.get_name() + "\n")

	pizza = ny_store.orderPizza("clam")
	print("Ethan ordered a " + pizza.get_name() + "\n")

	pizza = chicagoStore.orderPizza("clam")
	print("Joel ordered a " + pizza.get_name() + "\n")

	pizza = ny_store.orderPizza("pepperoni")
	print("Ethan ordered a " + pizza.get_name() + "\n")

	pizza = chicagoStore.orderPizza("pepperoni")
	print("Joel ordered a " + pizza.get_name() + "\n")

	pizza = ny_store.orderPizza("veggie")
	print("Ethan ordered a " + pizza.get_name() + "\n")

	pizza = chicagoStore.orderPizza("veggie")
	print("Joel ordered a " + pizza.get_name() + "\n")

if __name__ == '__init__':
    main()
