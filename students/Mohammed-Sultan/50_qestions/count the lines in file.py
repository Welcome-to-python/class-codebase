try:
    file = open("test.txt", "r")

    lines = file.readlines()

    print(len(lines))

    file.close()

except FileNotFoundError:
    print("File not found")