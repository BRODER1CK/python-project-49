#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
import prompt


def even_game():
    name = welcome_user()
    win_counter = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    while win_counter < 3:
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        even = random_number % 2 == 0
        if answer == 'yes':
            answer = True
        elif answer == 'no':
            answer = False
        else:
            answer = None
        if even == answer:
            print("Correct!")
            win_counter += 1
        else:
            if answer is None:
                return print(f"Let's try again, {name}!")
            elif not even:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")


def main():
    even_game()


if __name__ == '__main__':
    main()
