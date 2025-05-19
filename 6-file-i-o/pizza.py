import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    table_formatter(sys.argv[1])


def table_formatter(file):
    try:
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            table_data = list(reader)
            return tabulate(table_data, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
