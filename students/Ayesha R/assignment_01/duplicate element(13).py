lst = [1, 2, 2, 3, 4, 4]
duplicates = set()
for i in lst:
    if lst.count(i) > 1:
        duplicates.add(i)
print("Duplicates:", list(duplicates))
