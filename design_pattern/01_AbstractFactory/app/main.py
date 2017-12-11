from .pizza_store import PizzaStore
from .pizza_ingredient_factory.ny_ingredient_factory import NyIngredientFactory
from .pizza_ingredient_factory.chicago_ingredient_factory import ChicagoIngredientFactory

ny_factory = NyIngredientFactory()
ny_store = PizzaStore(ny_factory)

chicago_factory = ChicagoIngredientFactory()
chicago_store = PizzaStore(chicago_factory)

ny_pizza = ny_store.create_pizza()
ny_pizza.print()

chicago_pizza = chicago_store.create_pizza()
chicago_pizza.print()