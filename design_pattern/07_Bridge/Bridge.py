import abc

class Bridge(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def desenharCirculo(self, x, y, radius):
        pass

class DrawingApi1(Bridge):
    def desenharCirculo(x, y, radius):
        return ("Api1.circle at {}: {} radius {}".format(x,y,radius))

class DrawingApi2(Bridge):
    def desenharCirculo(x, y, radius):
        return ("Api2.circle at {}: {} radius {}".format(x,y,radius))

class Forma:
    x = 0
    y = 0
    radius = 0
    br = Bridge

    def __init__(self, X, Y, Radius, Br):
        self.x = X
        self.y = Y
        self.radius = Radius
        self.br = Br

    def desenharCirculo(self,pct):
        self.radius *= pct
        return (self.br.desenharCirculo(x, y, self.radius))

x = 1
y = 2
radius = 3
api1 = Forma(x, y, radius, DrawingApi1)
um = api1.desenharCirculo(2.5)
print(um)

x = 2
y = 3
radius = 8
api2 = Forma(x, y, radius, DrawingApi2)
dois = api2.desenharCirculo(2.5)
print(dois)

