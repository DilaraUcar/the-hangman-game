# THE HANGMAN GAME
The Hangman is a Python terminal based game, which runs in Code Institute mock terminal on Heroku.

A user can beat the game by trying to guess the correct word by following the game rules before they run out of attempts. Each incorrect answer adds to the hangman.

The live game can be found [here](https://the-hangman-game-p3-63bab5abcbcf.herokuapp.com/)

![Mockup](docs/mockup.jpeg)

## CONTENTS
- [How To Play](#how-to-play)
- [Features](#features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Bugs](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Unsolved Bugs](#unsolved-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Media](#media)

## HOW TO PLAY

![input-name-validation](docs/name-valid.jpeg)

In this version of the Hangman game, the user needs to put in their name and the game is then generated with a welcome message. 

![starts game](docs/welcome.jpeg)

First the user reads through the "How To Play" rules and can then start the game by guessing a letter. The user has 6 tries to guess the word by putting in correct letters. If not the user is notified with a message. The same letter can not be entered again and the user also gets notified if they do.

![validation](docs/incorrect.jpeg)

The user will also be notified if they have guessed correct letters and the world will be updated accordinly. If the player gets to close to losing the player will see the hangman with DANGER ZONE! underneath to make it clear that not many attempts to guess the word is left.

![correct](docs/correct.jpeg)

And lastly if user wins or looses its clearly printed on the screen with ASCII text art. The user is asked in the end if they would like to play again and then enter Y/N.

![loose](docs/game-over.jpeg)
![win](docs/win.jpeg)

If the user chooses to play again they are then redirected to enter a name again and the game starts all over again. If they choose not to they are presented with the message: "Thanks for playing! Goodbye."

![play-again](docs/restart.jpeg)

## FEATURES
- The computer ramdomly selects a word from the words list. The player cannot see this word but is instead presented with underscores for the amount of letters there is in the selected word, and the correct letter inputs.

- The computer accepts user input and gives responsive feedback with input validation and handles error on all inputs.

- User cannot enter a number, more than one letter, or the same letter twice and will be presented with a responsive feedaback message.

### Future Features
- Implementation of a game leaders so the players are saved to an external file and having a score system.

- Have different themes the player can choose from. Right now the theme is only animals.

- Have a difficulity option where the player can choose what level of difficulity they desire.

## TESTING
I have manually tested this project by doing the following:
- Giging invalid inputs to make sure the input validation is working correctly.
- Tested in my gitpod terminal and also in the Code Institute Heroku terminal
- Passed the code through a [PEP8 Python Validator.](https://pep8ci.herokuapp.com/#) All code have been appropietly corrected and is now passing through the validator with no problems.

### Bugs
#### Solved Bugs
- I had trouble with the ASCII art showing up weird in console. I fixed this by using Raw Strings consisting of an 'r' before the opening quote. I found this problem solver in [this website](https://realpython.com/python-hangman/#step-5-draw-the-hanged-man).

- I had problems with adding space between two strings. In those cases i added print statements between and that fixed the problem.

#### Unsolved Bugs
- No unsolved bugs remaining.

## DEPLOYMENT
Steps taken to deploy project to Heroku:
- Commit and push all code to GitHub from GitPod.
- Create an [Heroku](https://heroku.com) account.
- Click on Create New App.
- Add name to your app and choose your region.
- Navigate to settings and add Conf Vars PORT 8000 and Buildpacks Python and Node.js.
- Navigate to deploy on the top of the page and search github repo and the connect.
- Then at the bottom deploy from branch and wait for everything to load.
- Open live page and made sure no errors occured.

The live game can be viewed [here.](https://the-hangman-game-p3-63bab5abcbcf.herokuapp.com/)


## CREDITS
- All the content in the game is my own, but I used Google to find information about hangman game and to generate a list of animal words.

- The template for the deployable application was provided by [Code Institute - Template.](https://github.com/Code-Institute-Org/p3-template)

### Media
- [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&v=0&f=Big&t=The%20Hangman) - Logo art.
- [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=GAME%20OVER!) - Game Over art.
- [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=YOU%20WIN!) - You Win art.
- [Real Python](https://realpython.com/python-hangman/#step-5-draw-the-hanged-man) - to get an understanding of how to build hangman game.
- [W3Schools - Python](https://www.w3schools.com/python/) - for information about python.
- [YouTube](https://www.youtube.com) - to search for python art and hangman game examples.