def convert(input):
    input = input.replace(':)','🙂')
    input = input.replace(':(','🙁')
    return input

def main():
    print(convert(input("Text: ")))

main()
