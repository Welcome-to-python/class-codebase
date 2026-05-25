num = int(input("Enter a 3-digit number: "))

a = num % 10
b = (num // 10) % 10
c = num // 100

sum_digits = a + b + c

print("Sum of digits =", sum_digits)
