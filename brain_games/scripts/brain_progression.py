#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
import prompt


def brain_progression():
    name = welcome_user()
    win_counter = 0
    print("What number is missing in the progression?")
    while win_counter < 3:
        start = randint(0, 50)
        stop = randint(50, 100)
        step = randint(1, 5)
        length = randint(5, 10)
        nums_list = list(range(start, stop, step))[:length]
        random_index = randint(0, len(nums_list) - 1)
        result = nums_list[random_index]
        nums_list[random_index] = ".."
        question = " ".join(map(str, (nums_list)))
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
    brain_progression()


if __name__ == '__main__':
    main()
