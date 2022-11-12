from random import randint
from math import gcd


TASK = "Find the greatest common divisor of given numbers."


def game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f"{num1} {num2}"
    result = str(gcd(num1, num2))
    return question, str(result)
