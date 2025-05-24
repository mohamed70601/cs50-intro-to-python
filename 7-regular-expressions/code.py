import re


def main():
    code = input("Hexadecimall color code: ")

    pattern = r"^#[0-9a-fA-F]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


main()
