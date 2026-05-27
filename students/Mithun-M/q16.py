text = "python is fun and python is powerful"
words = text.split()
count = {w: words.count(w) for w in set(words)}
print(count)