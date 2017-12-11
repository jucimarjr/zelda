from .pizza_ingredient_factory import PizzaIngredientFactory
from ..pizza.dough.thin_crost_dough import ThinCrostDough
from ..pizza.clams.fresh_clams import FreshClams
from ..pizza.sauce.plum_tomato_sauce import PlumTomatoSauce
from ..pizza.cheese.mozzarella_cheese import MozzarellaCheese

class NyIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        dough = ThinCrostDough()
        return dough

    def create_cheese(self):
        cheese = MozzarellaCheese()
        return cheese

    def create_sauce(self):
        sauce = PlumTomatoSauce()
        return sauce

    def create_clams(self):
        clams = FreshClams()
        return clams