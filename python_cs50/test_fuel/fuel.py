def main():
    while True:
        text = input("Fraction: ")
        try:
            num = convert(text)
            break
        except (ValueError, ZeroDivisionError):
            pass

    gauge(num)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if round(x/y*100) > 100:
        raise ValueError
    return round(x/y*100)

def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()
