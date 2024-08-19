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
    date = input("Date: ")
    if date[:1].isalpha():
        try:
            x, year = date.split(",")
            year = year.strip()
            month, day = x.split(" ")
            year = int(year)
            if not 999 < year < 10000:
                raise ValueError
            day = int(day)
            if not 0 < day < 32:
                raise ValueError
            month = months.index(month) + 1
        except ValueError:
            pass
        else:
            print(f"{year}-{month:02}-{day:02}")
            break
    else:
        try:
            month, day, year = date.split("/")
            month = int(month)
            if not 0 < month < 13:
                raise ValueError
            day = int(day)
            if not 0 < day < 32:
                raise ValueError
            year = int(year)
            if not 999 < year < 10000:
                raise ValueError
        except ValueError:
            pass
        else:
            print(f"{year}-{month:02}-{day:02}")
            break
