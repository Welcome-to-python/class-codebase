text = input("Enter a string: ")

mid = len(text) // 2

first_half = text[:mid].upper()
second_half = text[mid:].lower()

result = first_half + second_half

print(result)
