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

def display_word(word, guessed_letters):
    """
    Creates a display string for the word, 
    replacing unguessed letters with underscores.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
