from brain_games.cli import welcome_user
import prompt


def engine(games):
    name = welcome_user()
    print(games.TASK)
    rounds = 3
    for round in range(rounds):
        question, result = games.game()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(result):
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'.")
            return print(f"Let's try again, {name}!")
    return print(f"Congratulations, {name}!")
