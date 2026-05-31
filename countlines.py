try:
    with open("file.txt") as f:
        print("Lines:", len(f.readlines()))
except FileNotFoundError:
    print("File not found")
