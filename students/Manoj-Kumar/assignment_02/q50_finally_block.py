
try:
    file = open("sample.txt", "r")

    content = file.readlines()

    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
    print("File closed successfully")