import abc
#class Decorator(metaclass=abc.ABCMeta):
#@abc.abstractmethod

class Animal(metaclass=abc.ABCMeta):
	def __init__(self, nome, idade):
		super(Animal, self).__init__()
		self.__nome = nome
		self.__idade = idade
	@abc.abstractmethod
	def falar(self):
		pass

	def getNome(self):
		return self.__nome

	def setNome(self, nome):
		self.__nome = nome

	def getIdade(self):
		return self.__idade

	def setIdade(self, idade):
		self.__idade = idade

	#nome = property(fget = getNome, fset = setNome)
	#idade = property(fget = getIdade, fset = setIdade)
	
class Gato(Animal):
	def __init__(self, nome, idade):
		super(Gato, self).__init__(nome, idade)

	def falar(self):
		print("O gato está miando.")

class Cachorro(Animal):
	def __init__(self, nome, idade):
		super(Cachorro, self).__init__(nome, idade)

	def falar(self):
		print("O cachorro está latindo.")


class Pet(Animal):
	def __init__(self, animal):
		super(Pet, self).__init__(animal.getNome(), animal.getIdade())
		self.animal = animal
	
	def falar(self):
		self.animal.falar()

	def getNome(self):
		return self.animal.getNome()
	
	def getIdade(self):
		return self.animal.getIdade()

	def setIdade(self, idade):
		self.animal.setIdade(idade)
	
	def setNome(self, nome):
		self.animal.setNome(nome)

if __name__ == '__main__':
	dog = Cachorro("Rex", 7)
	cat = Gato("Lili", 5)

	pet1 = Pet(dog)
	pet2 = Pet(cat)

	pet1.falar()
	pet2.falar()


#EXEMPLO DO LIVRO USE A CABEÇA
"""
Starbuzz coffee
Author: m1ge7
Date: 2014/03/25
"""

from abc import ABCMeta, abstractmethod


###############################################################################
# Beverages
###############################################################################

class Beverage:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):

    def __init__(self):
        self._description = "Dark Roast Coffee"

    def cost(self):
        return .99


class Espresso(Beverage):

    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return 1.99


class Decaf(Beverage):

    def __init__(self):
        self._description = "Decaf Coffee"

    def cost(self):
        return 1.05


###############################################################################
# Condiment decorators
###############################################################################

class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_description(self):
        pass


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return .10 + self._beverage.cost()


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self):
        return .20 + self._beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Soy"

    def cost(self):
        return .15 + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

    def cost(self):
        return .10 + self._beverage.cost()


###############################################################################
# Simulation
###############################################################################

if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))