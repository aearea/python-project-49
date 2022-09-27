#!/user/bin/evn python3


import prompt
import random
from brain_games.cli import welcome_user


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = random.randint(0, 10)
    print("Question:" + str(question))
    answer = prompt.string("Your answer: ")
    if (((question % 2 == 0) and (answer == "yes")) or ((question % 2 != 0) and (answer == "no"))):
        print("Correct!")
        return True
    else:
        print("Wrong answer")
        return False


def main():
    name = welcome_user()
    play_count = 0
    play_bool = False
    while True:
        play_bool = game()
        if not play_bool:
            return None
        else:
            play_count += 1
        if play_count == 3:
            print("Congratilation," + name)
            return None


if __name__ == "__main__":
    main()
