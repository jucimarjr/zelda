from equipment import Equipment

class FloppyDisk(Equipment):
    def __init__(self,name,power,netPrice,discountPrice):
        self.name = name
        self.power = power
        self.netPrice = netPrice
        self.discountPrice = discountPrice

    def Power(self):
        return self.power

    def NetPrice(self):
        return self.netPrice

    def DiscountPrice(self):
        return self.discountPrice

    def Accept(self,Visitor):
        Visitor.visitFloppyDisk(self);
