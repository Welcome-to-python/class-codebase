secret_number = 7

for attempt in range(3):

    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct Guess!")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

else:
    print("You ran out of attempts.")