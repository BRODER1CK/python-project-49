#!/usr/bin/env python3
import prompt


name = prompt.string('May I have your name? ')


def welcome_user():
    print(name)
    print(f"Hello, {name}")
