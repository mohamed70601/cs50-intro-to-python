def main():
    reply = input("Greeting: ").strip().lower()

    if reply.startswith("hello"):
        print("$0")
    elif reply.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
