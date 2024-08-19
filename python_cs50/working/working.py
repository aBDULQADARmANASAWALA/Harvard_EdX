import re
import sys

def main():
    print(convert(input("Time: ")))

def convert(s):
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    match = re.search(pattern, s)
    if match:
        hour1, hour2 = [int(match.group(i)) for i in [1,4]]
        min1 = int(match.group(2)) if match.group(2) else 0
        min2 = int(match.group(5)) if match.group(5) else 0
        time1, time2 = [match.group(i) for i in [3,6]]

        if 0<=min1<60 and 0<=min2<60 and 0<hour1<13 and 0<hour2<13:
            hour1 = (hour1 if hour1 == 12 else hour1 + 12) if time1 == "PM" else (0 if hour1 == 12 else hour1)

            hour2 = (hour2 if hour2 == 12 else hour2 + 12) if time2 == "PM" else (0 if hour2 == 12 else hour2)

            hour1, hour2, min1, min2 = [str(i).zfill(2) for i in [hour1, hour2, min1, min2]]
            return f"{hour1}:{min1} to {hour2}:{min2}"
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
