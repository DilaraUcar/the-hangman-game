import random
from game_art import hangman_graphics, logo, game_over, you_win

def get_word():
    """
    Get a random word from the words list
    """
    words = [
        "Giraffe",
        "Tiger",
        "Penguin",
        "Elephant",
        "Kangaroo",
        "Cheetah",
        "Dolphin",
        "Koala",
        "Gorilla",
        "Sloth",
        "Lemur",
        "Octopus",
        "Cat",
        "Rabbit",
        "Hamster"
        ]
        
    return random.choice(words).upper()


def display_word(word_to_guess, guessed_letters):
    """
    Creates a display string for the word,
    replacing unguessed letters with underscores.
    """
    display = ""
    for letter in word_to_guess:
        if letter.upper() in guessed_letters or not letter.isalpha():
            display += letter
        else:
            display += "_"

    # Join the characters in the 'display' string with spaces in between.
    return ' '.join(display)


def draw_hangman(incorrect_attempts):
    """
    Display hangman graphics based on incorrect attempts.
    """
    print(hangman_graphics[incorrect_attempts])


def validate_guess(guessed_letters):
    """
    Validate the user's letter input.
    Returns a letter or none if the input is invalid.
    """
    guess = input("Guess a letter:\n").upper().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return None

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        return None

    return guess


def hangman():
    """
    The Hangman game logic.
    """
    print(logo)
    word_to_guess = get_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    player_name = input("Please enter your name:\n").upper()
    print(f"HELLO {player_name}, WELCOME TO HANGMAN!\n")

    # Display rules on how to play
    print("HOW TO PLAY:\n")
    print("1. The theme is Animals")
    print("2. Guess letters to uncover the secret word.")
    print("3. You have a maximum of 6 incorrect attempts.")
    print("4. If you guess the word or run out of attempts, the game ends.\n")

    while incorrect_attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        # Add space between current_display and incorrect attempts
        print()

        # Find the set of incorrect letters by subtracting the set of uppercase letters
        # in the guessed letters from the set of uppercase letters in the target word.
        incorrect_letters = {letter for letter in guessed_letters} - set(word_to_guess.upper())
        print("Incorrect letters:", ', '.join(incorrect_letters))

        # Add space between incorrect letters and guess a letter
        print()
        
        guess = validate_guess(guessed_letters)

        if guess is None:
            continue

        guessed_letters.append(guess)

        if guess.upper() not in word_to_guess.upper():
            incorrect_attempts += 1
            draw_hangman(incorrect_attempts)
            print(f"Incorrect! You have {max_attempts - incorrect_attempts} attempts remaining\n")
        else:
            draw_hangman(incorrect_attempts)
            print("Correct guess!")

        if set(guessed_letters) >= set(word_to_guess.upper()):
            print(you_win)
            print(f"Congratulations, {player_name}! You guessed correrct:", word_to_guess)
            break

    if incorrect_attempts == max_attempts:
        print(game_over)
        print(f"Sorry, {player_name}, you ran out of attempts. The word was:", word_to_guess)

        # Adds a line of space
        print()


def play_again():
    """
    Ask the user if they want to play again, with a while loop that continues the game
    if the user wants to play again until they enter 'n'.
    """
    while True:
        response = input("Do you want to play again? (Y/N):\n").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please enter either 'Y' or 'N'.")

while True:
    hangman()
    if not play_again():
        print("Thanks for playing! Goodbye.")
        break