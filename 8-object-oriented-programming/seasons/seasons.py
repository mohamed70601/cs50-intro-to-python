from datetime import date
import sys
import inflect


def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    p = inflect.engine()

    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    current_day = date.today()
    diff = current_day - dt
    minutes = int(diff.total_seconds() / 60)

    return (f"{p.number_to_words(minutes, andword='')} minutes").capitalize()


if __name__ == "__main__":
    main()
