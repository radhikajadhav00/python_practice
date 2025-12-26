ch = input("Enter a character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a Vowel")
elif ch.isalpha():
    print("The character is a Consonant")
else:
    print("Invalid input")
