def main():

    items = {}

    while True:
        try:
            item = input("").strip().upper()
            if item == "DONE":
                break
            elif item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            break
    # sorted_items = sorted(items.items())
    # for key, value in sorted_items:
    #     print(f"{value} {key}")
    for item in sorted(items):
        print(f"{items[item]} {item}")


main()
