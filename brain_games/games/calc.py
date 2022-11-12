from random import randint
from random import choice


TASK = "What is the result of the expression?"


def game():
    operators = ["-", "+", "*"]
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice(operators)
    question = f"{num1} {operator} {num2}"
    if operator == "-":
        result = num1 - num2
    elif operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1 * num2
    return question, str(result)
