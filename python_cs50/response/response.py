from validator_collection import validators, checkers, errors

def main():
    try:
        email = validators.email(input("Email: "))
        print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()
