from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    question = randint(1, 100)
    if question % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return question, result
