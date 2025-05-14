def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    noVowels = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            noVowels += letter
    return noVowels


if __name__ == "__main__":
    main()
