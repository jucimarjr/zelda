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

	nome = property(fget = getNome, fset = setNome)
	idade = property(fget = getIdade, fset = setIdade)
	
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
