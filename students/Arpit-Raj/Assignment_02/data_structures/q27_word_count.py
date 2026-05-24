sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print("Word Count:", len(words))
print("Longest Word:", longest_word)
