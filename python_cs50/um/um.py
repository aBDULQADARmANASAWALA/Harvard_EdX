import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = " " + s + " "
    pattern = r"\Wum\W"
    match = re.findall(pattern, s, re.I)
    return len(match)


if __name__ == "__main__":
    main()
