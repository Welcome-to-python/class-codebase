# Compound Interest Program

P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
t = float(input("Enter time in years: "))
n = int(input("Enter number of times interest compounded per year: "))

A = P * (1 + (R / (100 * n))) ** (n * t)
CI = A - P

print("Compound Interest =", round(CI, 2))
print("Total Amount =", round(A, 2))