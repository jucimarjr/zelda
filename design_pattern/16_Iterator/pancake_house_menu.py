from menu import Menu
from menu_item import MenuItem


import java.util.ArrayList;
class PancakeHouseMenu(Menu):
	self.menu_items = []
 
	def __init__(self):
		self.menu_items = []
    
		addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", true,2.99)
 		addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", false, 2.99)
 		addItem("Blueberry Pancakes","Pancakes made with fresh blueberries, and blueberry syrup",true, 3.49)
 		addItem("Waffles","Waffles, with your choice of blueberries or strawberries",true, 3.59)

	def add_item(self, name, description,vegetarian, price):
		MenuItem menuItem = new MenuItem(name, description, vegetarian, price)
		menu_items.add(menuItem)
 
	def get_menu_items(self):
		return menu_items
  
	def create_iterator(self):
		return menu_items.iterator()
