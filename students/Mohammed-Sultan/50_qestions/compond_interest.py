P = float(input("Principal: "))
r = float(input("Rate: ")) / 100
t = float(input("Time: "))

A = P * (1 + r) ** t

print("Compound Interest =", round(A - P, 2))