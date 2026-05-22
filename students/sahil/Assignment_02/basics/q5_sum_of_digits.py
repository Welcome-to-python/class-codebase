number = int(input("Enter a three-digit number: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

sum_of_digits = digit1 + digit2 + digit3

print("Sum of digits:", sum_of_digits)
