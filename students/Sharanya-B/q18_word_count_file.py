try:
    with open(r"d:\Workspace\Python\class-codebase\students\Shranaya-B\sample.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Word count:", len(words))

except FileNotFoundError:
    print("File not found. Check the path.")