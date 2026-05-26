text = input("Enter a string: ").lower()

vowels = "aeiou"
frequency = {}

for vowel in vowels:
    frequency[vowel] = text.count(vowel)

print(frequency)