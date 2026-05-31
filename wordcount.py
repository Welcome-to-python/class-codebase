sentence = input("Enter sentence: ")
words = sentence.split()
print("Word count:", len(words))
print("Longest word:", max(words, key=len))
