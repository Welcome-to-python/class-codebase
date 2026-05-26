
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}

result = dict1.copy()

for key in dict2:
    if key in result:
        result[key] += dict2[key]
    else:
        result[key] = dict2[key]

print(result)