import sys


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        print(line_counter(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")


def line_counter(file):
    count = 0
    with open(file, "r") as f:
        for row in f:
            if row.strip() != "" and not row.lstrip().startswith("#"):
                count += 1
    return count


if __name__ == "__main__":
    main()
