s = input("Enter string: ").lower()
freq = {v: s.count(v) for v in "aeiou"}
print(freq)
