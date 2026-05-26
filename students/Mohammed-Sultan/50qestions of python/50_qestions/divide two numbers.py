try:
    a = int(input())
    b = int(input())

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
    