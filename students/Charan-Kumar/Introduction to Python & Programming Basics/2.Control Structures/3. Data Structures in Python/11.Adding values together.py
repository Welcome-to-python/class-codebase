d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}

result = d1.copy()

for k, v in d2.items():
    if k in result:
        result[k] += v
    else:
        result[k] = v

print(result)