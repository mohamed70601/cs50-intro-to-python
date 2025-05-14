def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(f"{percentage}%"))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        parts = fraction.split("/")
        x = int(parts[0])
        y = int(parts[1])

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round((x / y) * 100)
    except (ValueError, IndexError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return percentage


if __name__ == "__main__":
    main()
