from Menu import *

class Diner(Menu):

    def get_name(self):
        return "Pasta"

    def get_description(self):
        return "Spaghetti with Marinara sauce, and a slice of sourdough bread"

    def is_vegetarian(self):
        return True

    def get_price(self):
        return 3.89
