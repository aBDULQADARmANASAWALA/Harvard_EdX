def main():
    print("Output: " + shorten(input("Input: ")))


def shorten(word):
    test = ""
    for c in word:
        if c not in ['A', 'E', 'I', 'O', 'U' ,'a', 'e', 'i', 'o', 'u']:
            test += c
    return test


if __name__ == "__main__":
    main()
