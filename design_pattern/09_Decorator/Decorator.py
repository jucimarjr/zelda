#import abc
#class Decorator(metaclass=abc.ABCMeta):
#@abc.abstractmethod

class Animal:
	def __init__(self, nome, idade):
		super(Animal, self).__init__()
		self.__nome = nome
		self.__idade = idade

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


	'''@abstractmethod
    def falar(self):
    	pass'''

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
		self.animal = Animal()
		#super(Pet, self).__init__(animal.getNome(), animal.getIdade())
		super(Pet, self).__init__()
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


class Decorator:
	def __init__(self):
		self.cachorro = Cachorro("Rex", 9)
		self.gato = Gato ("Lili", 6)
		self.pet1 = Pet(cachorro)
		self.pet2 = Pet(gato)
		
		'''
			Animal dog = new Dog("Rex", 7);
			Animal cat = new Cat("Lili", 5);
			Animal pet1 = new Pet(dog);
			Animal pet2 = new Pet(cat);
			pet1.falar();
			pet2.falar();
		'''
	
	def run(self):
		pet1.falar();
		pet2.falar();

if __name__ == '__main__':
	decorator = Decorator()
	decorator.run()