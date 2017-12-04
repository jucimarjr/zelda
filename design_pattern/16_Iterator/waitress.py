from menu import Menu
from menu_item import MenuItem

class Waitress:
	self.menus = []
     
	def __init__(self,menus):
		self.menus = menus
   
	def print_menu(self):
		menu_iterator = menus.iterator()
		while True:
			menu = (Menu) menu_iterator.__next__()
			except StopIteration:
			break
   
	def print_menu(self, iterator):
		while True:
			menuItem = (MenuItem) iterator.__next__()
			print(menuItem.getName() + ", ")
			print(menuItem.getPrice() + " -- ")
			println(menuItem.getDescription())
			except StopIteration:
				break
