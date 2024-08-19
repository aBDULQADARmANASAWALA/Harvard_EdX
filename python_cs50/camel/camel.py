snake = ""

for c in input("camelCase: "):
    snake += "_" + c.lower() if c.isupper() else c

print("snake_case:", snake)
