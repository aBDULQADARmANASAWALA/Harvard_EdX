x, z, y = input("Expression: ").strip().split(" ")
# hello this is a comment

""" hello this is a docstring """


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
