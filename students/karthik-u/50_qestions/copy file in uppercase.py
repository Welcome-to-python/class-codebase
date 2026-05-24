file1 = open("input.txt", "r")
file2 = open("output.txt", "w")

for line in file1:
    file2.write(line.upper())

file1.close()
file2.close()