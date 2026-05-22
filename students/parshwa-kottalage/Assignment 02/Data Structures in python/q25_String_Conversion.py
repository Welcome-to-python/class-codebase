
text = input("Enter a string: ")

middle = len(text) // 2

first = text[:middle].upper()
second = text[middle:].lower()

result = first + second

print(result)