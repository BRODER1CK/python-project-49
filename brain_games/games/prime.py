from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    question = randint(2, 100)
    for num in range(2, int(question / 2 + 1)):
        if question % num == 0:
            prime = False
        else:
            prime = True
        if prime is True:
            result = "yes"
        else:
            result = "no"
    return question, result
