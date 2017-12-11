class Tickets():
    def __init__(self, name, quantity = 1):
        self.name = name
        self.quantity = quantity

    def print(self):
        print(str(self.quantity) + " ticket(s) for " + self.name)