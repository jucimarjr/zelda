from Expression import Expression

class Variable(Expression):
	def __init__(self, name):
	    self.name = name

	def interpret(self, variables):
	    if(variables[self.name].interpret() == 0):
		    return 0
	    return variables[self.name].interpret()
