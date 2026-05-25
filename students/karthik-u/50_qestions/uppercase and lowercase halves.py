text = input()

mid = len(text) // 2

first = text[:mid].upper()
second = text[mid:].lower()

print(first + second)