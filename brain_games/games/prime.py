from random import randint
from math import sqrt


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    for num in range(2, int(question / 2 + 1)):
        if question % num == 0:
            return False
    return True


def game():
    question = randint(2, 100)
    if is_prime(question):
        result = "yes"
    else:
        result = "no"
    return question, result
