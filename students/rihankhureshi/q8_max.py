a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("Max:", a)
elif b >= c:
    print("Max:", b)
else:
    print("Max:", c)