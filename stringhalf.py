s = input("Enter string: ")
mid = len(s)//2
print(s[:mid].upper() + s[mid:].lower())