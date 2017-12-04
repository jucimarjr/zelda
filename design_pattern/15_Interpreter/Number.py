from Expression import Expression

class Number(Expression):
	def __init__(self, number):
	    self.number = number

	def interpret(self):
	    return self.number
