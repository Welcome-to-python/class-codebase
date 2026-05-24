secret = 7

for i in range(3):
    guess = int(input())

    if guess == secret:
        print("Correct")
        break
else:
    print("Out of attempts")