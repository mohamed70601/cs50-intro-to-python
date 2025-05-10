import random
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    numbers = list(range(1, level + 1))
    random_num = random.choice(numbers)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess == random_num:
                print("Just right!")
                sys.exit()
            elif guess < random_num:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            print("Please enter a valid number")


main()
