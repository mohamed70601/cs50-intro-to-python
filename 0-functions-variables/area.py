def area(length, width):
    return length * width


def main():
    house = area(15, 25)
    yard = area(5, 10)
    total = house + yard

    print(str(total) + " square meters")


main()
