import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        tries = 0
        while tries < 3:
            print(f"{num1} + {num2} = ", end="")
            try:
                ans = int(input(""))
            except ValueError:
                pass
            else:
                if ans == num1 + num2:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
    print("Score: " + str(score))


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            match n:
                case 1 | 2 | 3:
                    return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, (10 ** level) - 1)
    else:
        return random.randint(10 ** (level - 1), (10 ** level) - 1)


if __name__ == "__main__":
    main()
