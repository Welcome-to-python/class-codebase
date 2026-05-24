text = input()

words = text.split()

longest = max(words, key=len)

print("Words:", len(words))
print("Longest:", longest)