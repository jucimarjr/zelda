from .pizza.pizza import Pizza

class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def create_pizza(self):
        pizza = Pizza(self.factory.create_dough(), self.factory.create_cheese(), \
                      self.factory.create_sauce(), self.factory.create_clams())
        return pizza