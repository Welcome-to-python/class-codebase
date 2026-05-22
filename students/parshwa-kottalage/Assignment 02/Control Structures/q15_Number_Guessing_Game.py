
correct_number = 7

for i in range(3):
    guess = int(input("Guess the number: "))

    if guess == correct_number:
        print("Correct Guess")
        break
else:
    print("You lost")