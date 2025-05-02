def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            print("Invalid coin.")

    if amount_due < 0:
        print(f"Change Owed: {-1 * amount_due}")
    else:
        print("Change Owed: 0")


main()
