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


def hangman():
    """
    Play the Hangman game.
    """
    print(logo)
    word_to_guess = get_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    player_name = input("Please enter your name:\n")
    print(f"Welcome to Hangman, {player_name}!")

    while incorrect_attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Word: ", current_display)
        # Find the set of incorrect letters by subtracting the set of uppercase letters
        # in the guessed letters from the set of uppercase letters in the target word.
        incorrect_letters = {letter for letter in guessed_letters} - set(word_to_guess.upper())
        print("Incorrect letters:", ', '.join(incorrect_letters))
        
        guess = input("Guess a letter:\n").upper().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess.upper() not in word_to_guess.upper():
            incorrect_attempts += 1
            draw_hangman(incorrect_attempts)
            print(f"Incorrect! You have {max_attempts - incorrect_attempts} attempts remaining")
        else:
            print("Correct guess!")

        if set(guessed_letters) >= set(word_to_guess.upper()):
            print(you_win)
            print(f"Congratulations, {player_name}! You guessed correrct:", word_to_guess)
            break

    if incorrect_attempts == max_attempts:
        print(game_over)
        print(f"Sorry, {player_name}, you ran out of attempts. The word was:", word_to_guess)
    
def play_again():
    """
    Ask the user if they want to play again.
    """
    return input("Do you want to play again? (Y/N): ").strip().lower() == 'y'

if __name__ == "__main__":
    while True:
        hangman()
        if not play_again():
            print("Thanks for playing! Goodbye.")
            break