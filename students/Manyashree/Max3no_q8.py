a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("Maximum =", a)
elif b >= a and b >= c:
    print("Maximum =", b)
else:
    print("Maximum =", c)
