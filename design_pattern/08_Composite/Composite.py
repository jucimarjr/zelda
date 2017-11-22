import abc

class Componente(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def getPrecoCusto(self):
        pass

    @abc.abstractmethod
    def getPrecoLucroMinimo(self):
        pass

    @abc.abstractmethod
    def getPrecoLucroMaximo(self):
        pass

class ComponenteComposite(Componente):

    def __init__(self):
        self._children = set()

    def add(self, componente):
        self._children.add(componente)

class Computador(ComponenteComposite):
    
    def getPrecoCusto(self):
        print("Calculando Preço de custo da composição")
        preco = 0
        for child in self._children:
            preco += child.getPrecoCusto()
        return preco

    def getPrecoLucroMinimo(self):
        print("calculando preco com o lucro minimo da composição")
        preco = 0
        for child in self._children:
            preco += child.getPrecoLucroMinimo()
        return preco

    def getPrecoLucroMaximo(self):
        print("calculando preco com o lucro maximo da composição")
        preco = 0
        for child in self._children:
            preco += child.getPrecoLucroMaximo()
        return preco

class CPU(Componente):
    
    def getPrecoCusto(self):
        return 300

    def getPrecoLucroMinimo(self):
        return 400

    def getPrecoLucroMaximo(self):
        return 600

class HardDisk(Componente):
    
    def getPrecoCusto(self):
        return 100

    def getPrecoLucroMinimo(self):
        return 120

    def getPrecoLucroMaximo(self):
        return 200

class Memoria(Componente):
    
    def getPrecoCusto(self):
        return 50

    def getPrecoLucroMinimo(self):
        return 60

    def getPrecoLucroMaximo(self):
        return 120

class PlacaMae(ComponenteComposite):
    
    def getPrecoCusto(self):
        print("Calculando Preço de custo da composição")
        preco = 100
        for child in self._children:
            preco += child.getPrecoCusto()
        return preco

    def getPrecoLucroMinimo(self):
        print("calculando preco com o lucro minimo da composição")
        preco = 150
        for child in self._children:
            preco += child.getPrecoLucroMinimo()
        return preco

    def getPrecoLucroMaximo(self):
        print("calculando preco com o lucro maximo da composição")
        preco = 200
        for child in self._children:
            preco += child.getPrecoLucroMaximo()
        return preco

comp = Computador()

pl = PlacaMae()

mem1 = Memoria()
mem2 = Memoria()
cpu = CPU()

pl.add(mem1)
pl.add(mem2)
pl.add(cpu)
comp.add(pl)

hd1 = HardDisk()
hd2 = HardDisk()

comp.add(hd1)
comp.add(hd2)

print("Calculando preço de custo da composição")
print("Valor: {}".format(comp.getPrecoCusto()))

print("Calculando preço de custo da composição")
print("Valor: {}".format(comp.getPrecoLucroMinimo()))

print("Calculando preço de custo da composição")
print("Valor: {}".format(comp.getPrecoLucroMaximo()))
