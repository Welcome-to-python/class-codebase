l1 = [1,2,3]
l2 = [2,3,4]
c = []
for i in l1:
    if i in l2 and i not in c:
        c.append(i)
print(c)
