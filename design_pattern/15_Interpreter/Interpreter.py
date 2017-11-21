class Expression():
    def interpret(self):
        pass

class Plus(Expression):

    def __init__(self, left, right):
        self.leftOperand = left
        self.rightOperand = right

    def interpret(self, variables):
        return self.leftOperand.interpret(variables) + self.rightOperand.interpret(variables)

class Minus:

    def __init__(self, left, right):
        self.leftOperand = left
        self.rightOperand = right

    def interpret(self, variables):
        return self.leftOperand.interpret(variables) - self.rightOperand.interpret(variables)


class Number(Expression):
	def __init__(self, number):
	    self.number = number

	def interpret(self, variables):
	    return number


class Variable(Expression):

	def __init__(self, name):
	    self.name = name


	def interpret(self, variables):
	    if(variables[self.name] == 0):
		    return 0
	    return variables[self.name]

class Evaluator(Expression):

    syntaxTree = Expression()
    def __init__(self, expression):

        expressionStack = []

        for i in range(len(expression)):
            if  expression[i] == "+" :
                subExpression = Plus (expressionStack.pop(), expressionStack.pop())
                expressionStack.append( subExpression )

            elif expression[i] == "-":
                right = expressionStack.pop()
                left = expressionStack.pop()

                subExpression = Minus(left, right)
                expressionStack.append( subExpression )
            elif expression[i] != ' ':
                expressionStack.append(Variable(expression[i]))

        self.syntaxTree = expressionStack.pop()

    def interpret(self, context):
        return self.syntaxTree.interpret(context)



def InterpreterExample():

	
    expression = "w x z - +"


    sentence = Evaluator(expression)

    variables = dict (w=5, x=10, z=42)


    result = sentence.interpret(variables)
    print(result)



InterpreterExample()