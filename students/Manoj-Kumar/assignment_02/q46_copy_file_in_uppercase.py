
file1 = open("input.txt", "r")

content = file1.read()

file2 = open("output.txt", "w")

file2.write(content.upper())

print("Content copied")

file1.close()
file2.close()