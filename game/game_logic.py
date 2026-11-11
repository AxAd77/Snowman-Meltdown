import random

from game.ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state."""
    print(STAGES[mistakes])

    word_display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(word_display)


def play_game():
    """Run the Snowman Meltdown game."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1 and not all(
        letter in guessed_letters for letter in secret_word
    ):
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

        display_game_state(mistakes, secret_word, guessed_letters)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You saved the snowman!")
    else:
        print("Game over! The snowman melted!")
        print("The secret word was:", secret_word)
