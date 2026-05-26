num = int(input("Enter a 3-digit number: "))
total = (num // 100) + (num // 10 % 10) + (num % 10)
print("Sum of digits:", total)
