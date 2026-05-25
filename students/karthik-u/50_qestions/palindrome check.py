text = input()

rev = ""

for i in text:
    rev = i + rev

print(text == rev)