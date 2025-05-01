def main():

    words = {"HAIR": 4, "CHAIR": 5, "PAIR": 4, "GRAPHIC": 7}

    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            words.clear()
            print("You've won!!!")
        if guess in words.keys():
            point = words.pop(guess)
            print(f"Good job! You scored {point} points.")

    # for word in words:
    #     print(f"{word} was worth {words[word]} points.")

    # for word, key in words.items():
    #     print(f"{word} was worth {key} points")


main()
