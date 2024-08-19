while(True):
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        percent = x / y * 100
        if (percent > 100):
            raise ValueError
    except (ValueError, ZeroDivisionError):
        pass
    else:
        match percent:
            case _ if percent >= 99:
                print("F")
            case _ if percent <= 1:
                print("E")
            case _ :
                print(f"{round(percent)}%")
        break
