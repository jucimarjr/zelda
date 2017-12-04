 from menu_item import MenuItem

 class DinerMenuIterator (Iterator<MenuItem>) :
	self.list = []
	self.position = 0
 
	def __init__(self, list):
		self.list = list
 
	def next(self):
		menu_item = list[position]
		self.position = self.position + 1
		return menu_item
 
	def has_next(self):
		if position >= len(list) or list[position] == None :
			return False
		else :
			return True
 
	def remove(self) :
		if position <= 0:
			print("You can't remove an item until you've done at least one next()")

		if list[position-1] != None :
			for  i in range(position-1, list.length-1):
				list[i] = list[i+1];
			list[list.length-1] = None;
