source_file = open("sample.txt", "r")

content = source_file.read()

source_file.close()

target_file = open("uppercase.txt", "w")

target_file.write(content.upper())

target_file.close()

print("Uppercase content written successfully.")