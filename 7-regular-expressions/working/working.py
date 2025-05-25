import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    h1 = int(match.group(1))
    m1 = int(match.group(2)) if match.group(2) else 0
    period1 = match.group(3)

    h2 = int(match.group(4))
    m2 = int(match.group(5)) if match.group(5) else 0
    period2 = match.group(6)

    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Hour must be between 1 and 12")
    if not (0 <= m1 <= 59) or not (0 <= m2 <= 59):
        raise ValueError("Minute must be between 00 and 59")

    h1 = h1 % 12 if period1 == "AM" else h1 % 12 + 12
    h2 = h2 % 12 if period2 == "AM" else h2 % 12 + 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
