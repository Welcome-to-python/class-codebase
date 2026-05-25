dict1 = {"a": 10, "b": 20}
dict2 = {"b": 5, "c": 15}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)