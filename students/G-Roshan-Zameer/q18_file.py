with open("file.txt", "r") as f:
    data = f.read()
    words = data.split()
    print("Word count:", len(words))