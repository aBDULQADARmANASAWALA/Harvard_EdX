x, z, y = input("Expression: ").strip().split(" ")

match z:
    case "+":
        ans = int(x) + int(y)
        print(f"{ans:.1f}")
    case "-":
        ans = int(x) - int(y)
        print(f"{ans:.1f}")
    case "*":
        ans = int(x) * int(y)
        print(f"{ans:.1f}")
    case "/":
        ans = int(x) / int(y)
        print(f"{ans:.1f}")
