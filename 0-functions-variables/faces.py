def main():
    emoji = str(input("Happy or sad? "))
    print(convert(emoji))


def convert(face):
    return face.replace(":)", "🙂").replace(":(", "🙁")


main()
