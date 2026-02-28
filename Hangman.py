import random

words = ["programming", "python", "gaming", "computer", "guessing"]
secret_word = random.choice(words)

guessed_letters = []
lives = 6

print("Welcome to Hangman game 🎮!\n")
print("The word to guess has", len(secret_word), "letters.\n")

while lives > 0:

    print("You have", lives, "lives left.\n")

    # Build display word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(display_word)

    # ✅ CHECK WIN HERE (BEFORE ASKING INPUT)
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        break

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("\nYou already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("\nGood guess!\n")
    else:
        print("\nWrong guess!\n")
        lives -= 1

if lives == 0:
    print("\nYou lost! The word was:", secret_word)