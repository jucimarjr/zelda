from MenuComponent import *

class Menu(MenuComponent):

    def __init__(self):
        self._children = set()

    def get_name(self):
        name = ""
        for child in self._children:
            name += child.get_name()
        return name

    def get_description(self):
        description = ""
        for child in self._children:
            description += child.get_description()
        return description

    def get_price(self):
        price = 0
        for child in self._children:
            price += child.get_price()
        return price

    def is_vegetarian(self):
        vegetarian = False
        for child in self._children:
            vegetarian += child.is_vegetarian()
        return vegetarian

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)
