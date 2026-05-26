s = input("Enter a string: ")

mid = len(s) // 2

result = s[:mid].upper() + s[mid:].lower()

print(result)