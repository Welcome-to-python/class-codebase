d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}
merged = d1.copy()
for k,v in d2.items():
    merged[k] = merged.get(k,0) + v
print(merged)
