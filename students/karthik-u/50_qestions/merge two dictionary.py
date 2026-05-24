d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}

result = d1.copy()

for i in d2:
    if i in result:
        result[i] += d2[i]
    else:
        result[i] = d2[i]

print(result)