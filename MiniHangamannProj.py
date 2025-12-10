import random

words = ["python", "coding", "github", "program", "developer"]
word = random.choice(words)

guesses = ""
attempts = 6

while attempts > 0:
    display = ""
    for char in word:
        display += char if char in guesses else "_"

    print("Word:", display)

    if display == word:
        print("You guessed it!")
        break

    guess = input("Enter a letter: ").lower()
    guesses += guess

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over. Word was:", word)
