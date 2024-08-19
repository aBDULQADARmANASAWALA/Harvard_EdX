def main():
    ...

def is_valid(s):
    # start with at least 2 letters
    for c in s[:2]:
        if not str(c).isalpha():
            return False

    # max of 6 chars and min of 2 chars
    if not 1 < len(s) < 7:
        return False

    # numbers must be at end, first number used cannot be a ‘0’
    new_number = False
    for c in s:
        if c == '0' and not new_number:
            return False
        elif str(c).isdecimal() and not new_number:
            new_number = True
        elif str(c).isalpha() and new_number:
            return False

    # no periods, spaces, or punctuation
    for c in s:
        if not str(c).isalnum():
            return False
    return True

if __name__ == "__main__":
    main()
