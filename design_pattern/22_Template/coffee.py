from caffeine_beverage import CaffeineBeverage

class Coffee(CaffeineBeverage):

    def prepareRecipe(self):
        self.boilWater()
        self.brewCoffeeGrinds()
        self.pourInCup()
        self.addSugarAndMilk()
        pass

    def boilWater(self):
        print("Boiling Water")
        pass

    def brewCoffeeGrinds(self):
        print("Dripping Coffee through filter")
        pass

    def pourInCup(self):
        print("Pouring into cup")
        pass

    def addSugarAndMilk(self):
        print("Adding Sugar and Milk")
        pass
