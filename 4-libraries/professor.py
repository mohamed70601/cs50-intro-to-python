import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        for _ in range(3):
            print(f"{x} + {y} = ", end="")
            try:
                answer = int(input())
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {result}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


# changed return value to an int instead of a tuple
def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")
    return n


if __name__ == "__main__":
    main()
