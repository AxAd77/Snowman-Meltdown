import random

from game.ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""

    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state."""

    print()
    print("***** Snowman Meltdown *****")
    print(STAGES[mistakes])

    word_display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(word_display)
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or '-'}")
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")


def get_valid_guess(guessed_letters):
    """Get a valid letter from the player."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess


def is_word_guessed(secret_word, guessed_letters):
    """Check if all letters of the secret word have been guessed."""
    return all(
        letter in guessed_letters for letter in secret_word
    )


def play_round():
    """Run one round of Snowman Meltdown."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = set()

    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < MAX_MISTAKES and not is_word_guessed(
            secret_word, guessed_letters
    ):
        guess = get_valid_guess(guessed_letters)

        if guess is None:
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

        display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_guessed(secret_word, guessed_letters):
        print("Congratulations! You saved the snowman!")
    else:
        print("Game over! The snowman melted!")
        print("The secret word was:", secret_word)


def ask_play_again():
    """Ask the player if they want to play again."""
    while True:
        play_again = input("Play again? (y/n): ").lower()

        if play_again not in ("y", "n"):
            print("Please enter 'y' or 'n'.")
            continue

        return play_again == "y"


def play_game():
    """Run the Snowman Meltdown game."""
    print("Welcome to Snowman Meltdown!")

    while True:
        play_round()

        if not ask_play_again():
            print("Thanks for playing Snowman Meltdown!")
            break
