def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        # debugged
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
