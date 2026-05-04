lst = [1, 2, 3, 2, 4, 1, 5]
dup = []
for i in lst:
    if lst.count(i) > 1 and i not in dup:
        dup.append(i)
print(dup)