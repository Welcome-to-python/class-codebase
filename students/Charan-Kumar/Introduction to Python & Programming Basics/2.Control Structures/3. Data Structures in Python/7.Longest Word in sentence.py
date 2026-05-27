s = input("Enter a sentence: ")

words = s.split()

print("Number of words =", len(words))
print("Longest word =", max(words, key=len))