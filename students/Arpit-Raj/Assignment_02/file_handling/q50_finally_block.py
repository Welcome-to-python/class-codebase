path = r"D:/Workspace/Python_of_Classmates/Arpit_python/class-codebase/students/Arpit-Raj/Assignment_02/file_handling/sample.txt"

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