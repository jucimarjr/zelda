"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""
import abc

class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Calcular(self, A, B):
        pass

class Somar(Strategy):
    def Calcular(A, B):
        return(A + B)

class Subtrair(Strategy):
    def Calcular(A, B):
        return(A - B)

class Operar:
    a = 0
    b = 0
    op = Strategy

    def __init__(self, A, B, Op):
        self.a = A
        self.b = B
        self.op = Op

    def Calcular(self):
        return(self.op.Calcular(a, b))


a = 10
b = 5
somar = Operar(a, b, Somar)
soma = somar.Calcular()
print('Soma: ', soma)

subtrair = Operar(a, b, Subtrair)
subtracao = subtrair.Calcular()
print('Subtração: ', subtracao)
