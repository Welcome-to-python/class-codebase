try:

    file = open("sample.txt", "r")

    lines = file.readlines()

    print("Number of lines:", len(lines))

    file.close()

except FileNotFoundError:

    print("File not found")
