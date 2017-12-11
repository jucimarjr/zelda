class Pizza:
    def __init__(self, dough, cheese, sauce, clams):
        self.dough = dough
        self.cheese = cheese
        self.sauce = sauce
        self.clams = clams

    def print(self):
        print("This is a pizza composed of " + self.dough.name + ", " + self.cheese.name + ", " + \
        self.sauce.name + " and " + self.clams.name)