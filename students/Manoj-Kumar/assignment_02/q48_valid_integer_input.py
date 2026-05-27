
while True:

    try:
        num = int(input("Enter integer: "))

        print("Valid Number =", num)
        break

    except ValueError:
        print("Invalid input")