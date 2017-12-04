from Number import Number
from Evaluator import Evaluator

def InterpreterExample():
    expression = "w x z - +"
    sentence = Evaluator(expression)

    variables = dict (w = Number(5), x = Number(10), z = Number(42))

    result = sentence.interpret(variables)
    print(result)

InterpreterExample()
