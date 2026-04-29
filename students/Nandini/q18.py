file = open("sample.txt", "r")
text = file.read()

words = text.split()
print("Word count:", len(words))

file.close()