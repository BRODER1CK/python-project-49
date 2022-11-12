#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.cli import welcome_user
import prompt


def brain_gcd():
    name = welcome_user()
    win_counter = 0
    print("Find the greatest common divisor of given numbers.")
    while win_counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        question = f"{num1} {num2}"
        result = str(gcd(num1, num2))
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if str(answer) == str(result):
            print("Correct!")
            win_counter += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
