from .pizza_ingredient_factory import PizzaIngredientFactory
from ..pizza.dough.thick_crost_dough import ThickCrostDough
from ..pizza.clams.frozen_clams import FrozenClams
from ..pizza.sauce.marinara_sauce import MarinaraSauce
from ..pizza.cheese.reggiano_cheese import ReggianoCheese

class ChicagoIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        dough = ThickCrostDough()
        return dough

    def create_cheese(self):
        cheese = ReggianoCheese()
        return cheese

    def create_sauce(self):
        sauce = MarinaraSauce()
        return sauce

    def create_clams(self):
        clams = FrozenClams()
        return clams