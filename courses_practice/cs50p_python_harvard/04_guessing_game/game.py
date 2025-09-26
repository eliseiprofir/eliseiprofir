import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

generate = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < generate:
                print("Too small!")
            if guess > generate:
                print("Too large!")
            if guess == generate:
                print("Just right!")
                break
    except:
        pass