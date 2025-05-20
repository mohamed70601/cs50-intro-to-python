import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Can't read file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Can't write file")
    else:
        convert(sys.argv[1], sys.argv[2])


def convert(in_read, out_write):
    with open(in_read, "r") as f1, open(out_write, "w", newline="") as f2:
        reader = csv.DictReader(f1)
        writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].rsplit(", ")
            house = row["house"]
            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()
