due = 50

while (True):
    if due <= 0:
        print(f"Change Owed: {due * (-1)}")
        break

    print(f"Amount Due: {due}")

    match int(input("Insert Coin: ")):
        case 25:
            due -= 25
        case 10:
            due -= 10
        case 5:
            due -= 5
