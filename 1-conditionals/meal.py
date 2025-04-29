def main():
    theTime = input("What time is it? ")
    x = convert(theTime)

    if 7.0 <= x <= 8.0:
        print("breakfast time")
    elif 12.0 <= x <= 13.0:
        print("lunch time")
    elif 18.0 <= x <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    # time = str(time)
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    time = hours + (minutes / 60)
    return time


if __name__ == "__main__":
    main()
