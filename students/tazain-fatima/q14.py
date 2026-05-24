n = int(input())
p = True
if n<=1:
    p=False
for i in range(2,n):
    if n%i==0:
        p=False
        break
print("Prime" if p else "Not Prime")
