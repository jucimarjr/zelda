import abc

class MenuComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_description(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_price(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_vegetarian(self):
        raise NotImplementedError
