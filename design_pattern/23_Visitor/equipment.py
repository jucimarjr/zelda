import abc

class Equipment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Power(self):
        pass

    @abc.abstractmethod
    def NetPrice(self):
        pass
    
    @abc.abstractmethod
    def DiscountPrice(self):
        pass

    @abc.abstractmethod
    def Accept(self):
        pass
