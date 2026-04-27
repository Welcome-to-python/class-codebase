string = input("Enter a string: ")

print("Duplicate characters are:")

for i in range(len(string)):
    count = 0
    
    for j in range(i + 1, len(string)):
        if string[i] == string[j] and string[i] != ' ':
            count = count + 1

    if count > 0:
        print(string[i])