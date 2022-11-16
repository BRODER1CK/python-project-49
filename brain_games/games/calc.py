from random import randint
from random import choice
import operator


TASK = "What is the result of the expression?"


def game():
    """Takes two random numbers and operator, then return it."""
    operators = ["-", "+", "*"]
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operators = choice(operators)
    question = f"{num1} {operators} {num2}"
    if operators == "-":
        result = operator.sub(num1, num2)
    elif operators == "+":
        result = operator.add(num1, num2)
    elif operators == "*":
        result = operator.mul(num1, num2)
    return question, str(result)
