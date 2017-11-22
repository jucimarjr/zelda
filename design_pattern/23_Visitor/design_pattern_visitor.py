import abc

class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def falar(self,text):
		pass
	
	@abc.abstractmethod
	def correr(self,text):
		pass
	
	@abc.abstractmethod
	def accept(self,visitor):
		pass


class Cat(Animal):
	def falar(self,text):
		print(text)
	
	def correr(self,text):
		print(text)
	
	def accept(self,visitor):
		visitor.visitCat(self)

class Dog(Animal):
	def falar(self,text):
		print(text)
	
	def correr(self,text):
		print(text)
	
	def accept(self,visitor):
		visitor.visitDog(self)

class Visitor(metaclass=abc.ABCMeta):
	def visitDog(self,Dog):
		pass
	
	def visitCat(self,Cat):
		pass

class CorrerVisitor(Visitor):
	def visitDog(self,Dog):
		Dog.correr("O cachorro esta correndo!")
	
	def visitCat(self,Cat):
		Cat.correr("O gato esta correndo!")

class FalarVisitor(Visitor):
	def visitDog(self,Dog):
		Dog.falar("O cachorro esta latindo!")
	
	def visitCat(self,Cat):
		Cat.falar("O gato esta miando!")

def main():
	fala = FalarVisitor()
	corre = CorrerVisitor()

	dog = Dog()
	cat = Cat()

	dog.accept(fala)
	cat.accept(fala)

	dog.accept(corre)
	cat.accept(corre)

if __name__ == "__main__":
	main()
