import random

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
        
    return random.choice(words)

def display_word(word_to_guess, guessed_letters):
    """
    Creates a display string for the word, 
    replacing unguessed letters with underscores.
    """
    display = ""
    for letter in word_to_guess:
        if letter.lower() in guessed_letters or not letter.isalpha():
            display += letter + " "
        else:
            display += "_ "

    return display.strip()

def draw_hangman(incorrect_attempts):
    """
    Display hangman graphics based on incorrect attempts.
    """
    hangman_graphics = [
        # 0 incorrect attempts:
        """
        -------
        |   |
        |
        |
        |
        |
        |
        |
        |
        |
        -------
        """,
        # 1 incorrect attempt:
        """
        -------
        |   |
        |   O
        |
        |
        |
        |
        |
        |
        |
        -------
        """,
        # 2 incorrect attempts:
        """
        -------
        |   |
        |   O
        |  ---
        |   |
        |   |
        |
        |
        |
        |
        -------
        """,
        # 3 incorrect attempts:
        """
        -------
        |   |
        |   O
        |  ---
        | / |
        |   |
        |
        |
        |
        |
        -------
        """,
        # 4 incorrect attempts:
        """
        -------
        |   |
        |   O
        |  ---
        | / | \
        |   |
        |
        |
        |
        |
        -------
        """,
        # 5 incorrect attempts:
        """
        -------
        |   |
        |   O
        |  ---
        | / | \
        |   |
        |  ---
        | /
        |
        |
        -------
        """,
        # 6 incorrect attempts:
        """
        -------
        |   |
        |   O
        |  ---
        | / | \
        |   |
        |  ---
        | /   \
        |
        |
        -------
        """
    ]

    print(hangman_graphics[incorrect_attempts])

def hangman():
    """
    Play the Hangman game.
    """
    word_to_guess = get_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while incorrect_attempts < max_attempts:
        current_display = display_word(guessed_letters, word_to_guess)
        print("Word: ", current_display)
        incorrect_letters = [letter for letter in guessed_letters if letter not in word_to_guess.lower()]
        print("Incorrect letters:", ', '.join(incorrect_letters))
        
        guess = input("Please guess a letter:\n").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess.lower():
            incorrect_attempts += 1
            draw_hangman(incorrect_attempts)
            print("Incorrect! Attempts remaining:", max_attempts - incorrect_attempts)
        else:
            print("Correct guess!")

        if set(guessed_letters) >= set(word_to_guess.lower()):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if incorrect_attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)


if __name__ == "__main__":
    hangman()