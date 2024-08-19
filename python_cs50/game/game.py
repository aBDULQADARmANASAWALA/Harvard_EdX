from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess < number:
            print("Too small!")
        elif guess > 0 and guess > number:
            print("Too large!")
        elif guess == number:
            print("Just right!")
            break
    except ValueError:
        pass

