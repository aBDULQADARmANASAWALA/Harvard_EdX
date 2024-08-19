from sys import argv, exit

if len(argv) != 2 or not argv[1].endswith(".py"):
    print("Invalid command-line arguments")
    exit(1)

loc = 0
try:
    with open(argv[1]) as file:
        lines = file.readlines()
        for line in lines:
            if line.lstrip(" ").find("#") == 0:
                pass
            elif line.isspace():
                pass
            else:
                loc += 1
except FileNotFoundError:
    print("File not found")
    exit(1)

print(loc)
