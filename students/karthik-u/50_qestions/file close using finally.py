file = None

try:
    file = open("test.txt", "r")

    data = file.readlines()

    print(data)

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()

    print("File closed")