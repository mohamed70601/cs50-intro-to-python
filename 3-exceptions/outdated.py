def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        user_date = input("Date: ").strip()
        try:
            if "/" in user_date:
                m, d, y = user_date.split("/")
                m = int(m)
                d = int(d)
                y = int(y)
            else:
                md, y = user_date.split(",")
                m_str, d = md.strip().split()
                m = months.index(m_str.title()) + 1
                d = int(d)
                y = int(y)

            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04}-{m:02}-{d:02}")
                break
        except:
            continue


main()
