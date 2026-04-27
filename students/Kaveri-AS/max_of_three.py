a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Max is:", a)
elif b >= a and b >= c:
    print("Max is:", b)
else:
    print("Max is:", c)