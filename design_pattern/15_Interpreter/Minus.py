from Expression import Expression

class Minus(Expression):
    def __init__(self, left, right):
        self.leftOperand = left
        self.rightOperand = right

    def interpret(self, variables):
        return self.leftOperand.interpret(variables) - self.rightOperand.interpret(variables)
