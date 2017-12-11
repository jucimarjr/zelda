import abc

class PizzaIngredientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_dough():
        pass

    @abc.abstractmethod
    def create_cheese():
        pass

    @abc.abstractmethod
    def create_sauce():
        pass

    @abc.abstractmethod
    def create_clams():
        pass