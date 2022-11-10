#!/usr/bin/env python3
from random import randint
from random import choice
from brain_games.cli import welcome_user
import prompt


def brain_calc():
    name = welcome_user()
    win_counter = 0
    operators = ["-", "+", "*"]
    print("What is the result of the expression?")
    while win_counter < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operator = choice(operators)
        question = f"{number1} {operator} {number2}"
        if operator == "-":
            calculate = number1 - number2
        elif operator == "+":
            calculate = number1 + number2
        elif operator == "*":
            calculate = number1 * number2
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(calculate):
            print("Correct!")
            win_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{calculate}'")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()
