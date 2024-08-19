from pyfiglet import Figlet
from sys import argv, exit

match len(argv):
    case 1:
        f = Figlet()
    case 3:
        if argv[1] == "-f" or argv[1] == "--font":
            try:
                f = Figlet(font=argv[2])
            except IndexError:
                print("Invalid syntax.")
                exit(1)
        else:
            print("Invalid syntax.")
            exit(1)
    case _:
        print("Invalid syntax.")
        exit(1)

print("Output:", f.renderText(input("Input: ")))
