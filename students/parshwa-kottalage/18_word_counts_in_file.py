file = open("sample.txt", "r")

text = file.read()

words = text.split()

count = len(words)

print("Number of words:", count)

file.close()