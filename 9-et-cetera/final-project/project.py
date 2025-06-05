import sys, csv, os

FILENAME = "tasks.csv"


def main():
    if len(sys.argv) == 1:
        show_help()
        return
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            show_help()
        elif sys.argv[1] == "-a":
            add_task()
        elif sys.argv[1] == "-r":
            remove_task()
        elif sys.argv[1] == "-d":
            mark_task()
        elif sys.argv[1] == "-s":
            show_tasks()
        else:
            print("Unkown option. Use -h for help")
    except IndexError:
        sys.exit("Error: missing argument. Use -h for help")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}\nUse -h for help")


def show_help():
    print("Usage: python tasks.py [option]")
    print("\nOptions:")
    print("  -a      Add a new task")
    print("  -r      Remove a task")
    print("  -d      Mark a task as done")
    print("  -s      Show all tasks")
    print("  -h      Show this help message")


def add_task():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "Done"])

    task = input("Enter a new task: ").strip()

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task, "False"])

    print(f"Task [{task}] added.")


def remove_task():
    with open(FILENAME, newline="") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No tasks found.")
        return

    for i, row in enumerate(reader[1:], start=1):
        print(f"{i} - {row[0]} {'✅' if row[1] == 'True' else '❌'}")

    try:
        index = int(input("Task to remove: "))

        if 1 <= index < len(reader):
            reader.pop(index)
            print(f"Task: {index} removed")
        else:
            print("Invalid task number")
            return
    except ValueError:
        sys.exit("Invalid Input")

    # update tasks.csv
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)


def mark_task():
    with open(FILENAME, newline="") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("No tasks found.")
        return

    for i, row in enumerate(reader[1:], start=1):
        print(f"{i} - {row[0]} {'✅' if row[1] == 'True' else '❌'}")

    try:
        index = int(input("Task to mark done: "))
        if 1 <= index <= len(reader):
            if reader[index][1] == "True":
                print(f"Task: {index} has already been marked done")
            else:
                reader[index][1] = "True"
                print(f"Task: {index} marked done")
        else:
            print("Invalid task number")
            return
    except ValueError:
        sys.exit("Invalid input.")

    # update tasks.csv
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(reader)


def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            tasks = list(reader)

            if not tasks:
                print("No tasks found.")
                return

            for i, row in enumerate(tasks, start=1):
                status = "✅" if row["Done"] == "True" else "❌"
                # 15 min of debugging cuz i wrote "task" instead of "Task" :)
                print(f"{i} - {row['Task']} {status}")

    except FileNotFoundError:
        sys.exit("Tasks file not found.")


if __name__ == "__main__":
    main()
