from random import randint


TASK = "What number is missing in the progression?"


def game():
    """Takes random numbers in random range with random step
    and return it with one number incrypted."""
    start = randint(0, 100)
    stop = randint(start, 1000)
    step = randint(1, 5)
    length = randint(5, 10)
    nums_list = list(range(start, stop, step))[:length]
    random_index = randint(0, len(nums_list) - 1)
    result = nums_list[random_index]
    nums_list[random_index] = ".."
    question = " ".join(map(str, (nums_list)))
    return question, str(result)
