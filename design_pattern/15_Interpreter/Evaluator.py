from Expression import Expression
from Plus import Plus
from Minus import Minus
from Variable import Variable

class Evaluator(Expression):
    syntax_tree = Expression()

    def __init__(self, expression):
        expression_stack = []

        for i in range(len(expression)):
            if  expression[i] == "+" :
                sub_expression = Plus(expression_stack.pop(), expression_stack.pop())
                expression_stack.append( sub_expression )

            elif expression[i] == "-":
                right = expression_stack.pop()
                left = expression_stack.pop()

                sub_expression = Minus(left, right)
                expression_stack.append( sub_expression )

            elif expression[i] != ' ':
                expression_stack.append( Variable(expression[i]) )

        self.syntax_tree = expression_stack.pop()

    def interpret(self, context):
        return self.syntax_tree.interpret(context)
