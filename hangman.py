import random

# List of words for the game
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "science",
    "college",
    "internet",
    "database",
    "software"
]

# Hangman drawings for each stage
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def play_hangman():
    # Select a random word
    secret_word = random.choice(WORDS).upper()

    # Store guessed letters
    guessed_letters = set()

    # Track incorrect guesses
    mistakes = 0
    max_attempts = 6

    print("=" * 35)
    print("       WELCOME TO HANGMAN!")
    print("=" * 35)

    while mistakes < max_attempts:
        # Display the current hangman stage
        print(HANGMAN_STAGES[mistakes])

        # Display the hidden word
        displayed_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", displayed_word)
        print("Incorrect guesses remaining:", max_attempts - mistakes)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", secret_word)
            return

        print("Guessed letters:", " ".join(sorted(guessed_letters))
              if guessed_letters else "None")

        # Get the user's input
        guess = input("\nEnter a single letter: ").strip().upper()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).\n")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.add(guess)

        # Check the guess
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            mistakes += 1
            print("Incorrect guess! You lost one attempt.\n")

    # Display the final stage after six incorrect guesses
    print(HANGMAN_STAGES[mistakes])
    print("GAME OVER!")
    print("You ran out of attempts.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
