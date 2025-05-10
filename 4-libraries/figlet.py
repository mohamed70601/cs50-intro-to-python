from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid command-line argument(s)")
        if sys.argv[2] not in fonts:
            sys.exit("Invalid font")
        figlet.setFont(font=sys.argv[2])
    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))
    else:
        sys.exit("Invalid number of arguments")

    user_input = input("Input: ")
    print(figlet.renderText(user_input))


main()
