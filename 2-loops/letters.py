def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    for i in range(len(names)):
        print(i)
    #     print(write_letter(names[i], "Princess Peach"))

    for name in names:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f""" 
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()
