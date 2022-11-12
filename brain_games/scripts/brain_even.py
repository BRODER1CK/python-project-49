#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
import prompt


def even_game():
    name = welcome_user()
    win_counter = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    while win_counter < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            even = True
        else:
            even = False
        if even is True:
            result = "yes"
        else:
            result = "no"
        question = num
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
    even_game()


if __name__ == '__main__':
    main()
