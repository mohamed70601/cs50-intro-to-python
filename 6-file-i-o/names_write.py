name = input("What's your name? ")

with open("students.csv", "a") as file:
    file.write(f"{name}\n")
