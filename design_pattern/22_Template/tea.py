from caffeine_beverage import CaffeineBeverage

class Tea(CaffeineBeverage):

    def prepareRecipe(self):
        self.boilWater()
        self.steepTeaBag()
        self.pourInCup()
        self.addLemon()
        pass

    def boilWater(self):
        print("Boiling water")
        pass

    def steepTeaBag(self):
        print("Steeping the tea")
        pass

    def addLemon(self):
        print("Adding Lemon")
        pass

    def pourInCup(self):
        print("Pouring into cup")
        pass
