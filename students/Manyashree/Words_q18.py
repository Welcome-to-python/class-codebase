file = open("sample.txt", "r")
data = file.read()
words = data.split()

print("Word count =", len(words))
file.close()
