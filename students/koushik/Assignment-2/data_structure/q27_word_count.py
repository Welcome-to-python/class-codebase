sentence = input("Enter a sentence: ")

words = sentence.split()

count = len(words)
longest = max(words, key=len)

print("Word Count:", count)
print("Longest Word:", longest)