secret = 7
for attempt in range(3):
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
else:
    print("Out of attempts!")
