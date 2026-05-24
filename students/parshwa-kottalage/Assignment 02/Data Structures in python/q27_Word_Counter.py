
sentence = input("Enter sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Number of words =", len(words))
print("Longest word =", longest)