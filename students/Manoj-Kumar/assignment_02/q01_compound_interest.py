
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + (rate / 100) / n) ** (n * time)
compound_interest = amount - principal

print("compound_interest=",compound_interest)