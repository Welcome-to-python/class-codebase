with open("demo.txt", "w") as f:
    f.write("Hello File!")
with open("demo.txt", "r") as f:
    print(f.read())