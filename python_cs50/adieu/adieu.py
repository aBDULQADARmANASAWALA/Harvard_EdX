names = []
output = "Adieu, adieu, to "

while True:
    try:
        names.append(input("Name: ").strip().title())
    except EOFError:
        break


for name in names:
    match len(names) - names.index(name):
        # last name
        case 1:
            output += name
        # second last (if only 2 names)
        case 2 if len(names) == 2:
            output += name + " and "
        # second last for not only two names
        case 2 if len(names) != 2:
            output += name + ", and "
        # every other name
        case _:
            output += name + ", "

print("\n" + output)
