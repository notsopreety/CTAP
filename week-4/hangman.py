# Problem Set 2, hangman.py
# Name: Badaila Samir
# Collaborators: 
# Time spent: 1 hrs 30 min

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "*"
    return result


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available


def choose_letter_to_reveal(secret_word, available_letters):
    """
    Helper function suggested in PDF section 2.4.
    Chooses a random unguessed letter from the secret word.
    """
    choose_from = ""
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    return choose_from[new]


'''
Decomposition Explanation (Rubric Deliverable 4):
The game is broken down into small helper functions:
- has_player_won checks if all letters of the secret word have been guessed.
- get_word_progress builds the string with revealed letters and asterisks.
- get_available_letters creates the string of remaining letters to guess.
- choose_letter_to_reveal picks a missing letter at random for help mode.
This keeps the main hangman function simple and focused only on the game loop.
'''


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses_remaining = 10
    letters_guessed = []

    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_remaining > 0:
        print("--------------")
        if guesses_remaining == 1:
            print("You have 1 guess left.")
        else:
            print("You have", guesses_remaining, "guesses left.")

        available = get_available_letters(letters_guessed)
        print("Available letters:", available)

        guess = input("Please guess a letter: ")

        # Case 1: Help feature
        if with_help and guess == "!":
            if guesses_remaining >= 3:
                guesses_remaining -= 3
                revealed = choose_letter_to_reveal(secret_word, available)
                letters_guessed.append(revealed)
                print("Letter revealed:", revealed)
                print(get_word_progress(secret_word, letters_guessed))
            else:
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))

        # Case 2: Invalid input
        elif not (len(guess) == 1 and guess.isalpha()):
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))

        # Case 3: Valid letter input
        else:
            guess = guess.lower()
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            elif guess in secret_word:
                letters_guessed.append(guess)
                print("Good guess:", get_word_progress(secret_word, letters_guessed))
            else:
                letters_guessed.append(guess)
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                if guess in "aeiou":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

        # Check if the player has won
        if has_player_won(secret_word, letters_guessed):
            print("--------------")
            print("Congratulations, you won!")
            # Count unique letters in secret_word
            unique_letters = ""
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters += char
            score = (guesses_remaining + 4 * len(unique_letters)) + (3 * len(secret_word))
            print("Your total score for this game is:", score)
            return

    # Player ran out of guesses
    print("--------------")
    print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)
