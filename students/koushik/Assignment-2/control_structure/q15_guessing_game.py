secret_number = 7

for attempt in range(3):
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct Guess!")
        break
else:
    print("You lost the game.")