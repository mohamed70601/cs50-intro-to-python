def main():
    userText = input("Input: ")

    noVowels = ""

    for letter in userText:
        # this skips using else
        if letter not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            noVowels += letter

    print(f"Output: {noVowels}")


main()
