with open("file.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Word count:", len(words))
