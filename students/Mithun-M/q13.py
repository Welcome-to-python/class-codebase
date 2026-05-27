s = input("Enter text: ").lower()
vowels = "aeiou"
print("Vowel count:", sum(1 for ch in s if ch in vowels))