from Beverage import Beverage
from HouseBlend import HouseBlend
from DarkRoast import DarkRoast
from Espresso import Espresso
from Decaf import Decaf
from CondimentDecorator import CondimentDecorator
from Milk import Milk
from Mocha import Mocha
from Soy import Soy
from Whip import Whip

if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))