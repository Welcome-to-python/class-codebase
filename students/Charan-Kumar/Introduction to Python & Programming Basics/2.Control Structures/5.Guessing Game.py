secret = 11

for i in range(3):
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct Guess!")
        break
else:
    print("No attempts left")
