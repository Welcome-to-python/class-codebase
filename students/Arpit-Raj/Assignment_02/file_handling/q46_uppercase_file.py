path = r"D:/Workspace/Python_of_Classmates/Arpit_python/class-codebase/students/Arpit-Raj/Assignment_02/file_handling\sample.txt"

with open(path, "r") as source:

    content = source.read()

with open("uppercase.txt", "w") as target:

    target.write(content.upper())

print("Content written successfully")