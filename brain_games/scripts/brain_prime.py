#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
import prompt


def brain_prime():
    name = welcome_user()
    win_counter = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    while win_counter < 3:
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
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if str(answer) == str(result):
            print("Correct!")
            win_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
