string = input("Enter a string: ")

count = 0

for ch in string:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels =", count)