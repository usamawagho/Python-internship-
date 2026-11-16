import random

words = ["python", "coding", "laptop", "screen", "window"]
word = random.choice(words)

guessed = []
display = ["_"] * len(word)
wrong = 0
max_wrong = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.\n")

while wrong < max_wrong and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed))
    print("Attempts left:", max_wrong - wrong)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed:
        print("You already guessed that letter.\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong += 1
        print("Wrong guess!\n")

if "_" not in display:
    print("You win! The word was:", word)
else:
    print("Game over! The word was:", word)