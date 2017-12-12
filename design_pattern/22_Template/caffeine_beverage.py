import abc

class CaffeineBeverage():

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()
        pass

    @abc.abstractmethod
    def brew(self):
        pass

    @abc.abstractmethod
    def addCondiments(self):
        pass

    def boilWater(self):
        print("Boiling water")
        pass

    def pourInCup(self):
        print("Pouring into cup")
        pass