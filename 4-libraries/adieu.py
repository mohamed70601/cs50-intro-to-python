import inflect


def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input("Name: ").strip()
            if name:
                names.append(name)
    except EOFError:
        if names:
            print(f"Adieu, adieu, to {p.join(names)}")


main()
