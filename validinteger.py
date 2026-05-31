while True:
    try:
        num = int(input("Enter integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid, try again")
