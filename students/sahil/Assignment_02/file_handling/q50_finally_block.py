path = r"D:\Workspace\Python\class-codebase\students\sahil\Assignment_02\file_handling\sample.txt"

file = None

try:

    file = open(path, "r")

    content = file.readlines()

    print(content)

except FileNotFoundError:

    print("File not found")

finally:

    if file:

        file.close()

    print("File closed successfully")