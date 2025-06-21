import random

# 1. Predefined word list
words = ["apple", "bread", "candy", "lemon", "grape"]

# 2. Choose a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))

# 3. Game loop
while incorrect_guesses < max_guesses:
    guess = input("👉 Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! You have {max_guesses - incorrect_guesses} guesses left.")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word.strip())

    # Check win
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You guessed the word! You win!")
        break
else:
    print("💀 Game over! The word was:", secret_word)