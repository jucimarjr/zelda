from singleton import ChocolateBoiler

ChocolateBoiler().get_instance().fill()

chocolate_boiler = ChocolateBoiler().get_instance()

chocolate_boiler.print_boiler_state()

chocolate_boiler.boil()

chocolate_boiler.drain()
