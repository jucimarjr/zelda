from pancake_house_menu import PancakeHouseMenu
from diner_menu import DinerMenu
from menu import Menu
from waitress import Waitress


pancake_house_menu = PancakeHouseMenu()
dinerMenu = DinerMenu()
menus = []
menus.append(Menu)
menus.add(pancake_house_menu)
menus.add(dinerMenu)
waitress = Waitress(menus)
waitress.printMenu()