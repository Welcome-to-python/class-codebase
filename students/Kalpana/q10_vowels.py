s = input("Enter string: ")
count = 0
for i in s:
    if i.lower() in "aeiou":
        count += 1
print("Vowels:", count)