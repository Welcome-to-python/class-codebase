a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = []

for i in a:
    if i in b and i not in result:
        result.append(i)

print(result)