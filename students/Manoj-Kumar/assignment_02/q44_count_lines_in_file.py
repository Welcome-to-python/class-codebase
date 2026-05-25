
try:
    file = open("sample.txt", "r")

    lines = file.readlines()

    print("Total Lines =", len(lines))

    file.close()

except FileNotFoundError:
    print("File not found")