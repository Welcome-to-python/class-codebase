try:
    a = int(input("Enter number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
