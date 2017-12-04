from menu_item import MenuItem

 class DinerMenu(Menu):
	self.max_items = 6
	self.number_of_items = 0
	self.menu_items = []
  
	def __init__(self):
		add_item("Vegetarian BLT","(Fakin') Bacon with lettuce & tomato on whole wheat", true, 2.99)
		add_item("BLT","Bacon with lettuce & tomato on whole wheat", false, 2.99)
		add_item("Soup of the day","Soup of the day, with a side of potato salad", false, 3.29)
		add_item("Hotdog","A hot dog, with saurkraut, relish, onions, topped with cheese",false, 3.05)
		add_item("Steamed Veggies and Brown Rice","Steamed vegetables over brown rice", true, 3.99)
		add_item("Pasta","Spaghetti with Marinara Sauce, and a slice of sourdough bread", true, 3.89)
  
	def add_item(self, name, description,vegetarian, price) 
	{
		menu_item = MenuItem(name, description, vegetarian, price)
		if (number_of_items >= max_items) {
			print("Sorry, menu is full!  Can't add item to menu")
		} else {
			self.menu_items.append(menu_item) 
			self.number_of_items = self.number_of_items + 1
		}
	}
 
	def getmenu_items(self):
		return self.menu_items
	
  
	def create_iterator(self):
		return DinerMenuIterator(self.menu_items)
	
