# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    num = 0

    for char in secretWord:
        lettersGuessed_ = lettersGuessed[:]

        for i in range(len(lettersGuessed_)):
            if (char  == lettersGuessed_[i]):
                num += 1
                lettersGuessed[i] = 0
    if (num == len(secretWord)):
        flag = True
    else:
        flag = False

    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    show_list = []
    for i in range(len(secretWord)):
        show_list.append("_")

    for i in range(len(secretWord)):
        for j in range(len(lettersGuessed)):
            if(secretWord[i] == lettersGuessed[j]):
                show_list[i] = secretWord[i]

    show_str = ""
    for k in range(len(show_list)):
        show_str += show_list[k]

    return show_str


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AvailableLetters = ""
    for char in string.ascii_lowercase:
        if((char not in lettersGuessed) and (char not in AvailableLetters)):
             AvailableLetters += char
    return AvailableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    mistakesMade = 0
    guess_time = 8
    lettersGuessed = []
    lettersGuessed_correct = []


    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) + " letters long")

    while(True):
        if(guess_time == 0):
            print("-----------")
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break

        if("_" not in getGuessedWord(secretWord, lettersGuessed_correct)):
            print("-----------")
            print("Congratulations, you won!")
            break

        print("-----------")
        print("You have "+ str(guess_time) +" guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))

        input_letter = input("Please guess a letter: ")
        #lettersGuessed.append(input_letter)  # 写错地方了

        if(input_letter in lettersGuessed_correct or input_letter in lettersGuessed):
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed_correct))
            #print("-----------")
            continue            # !!!


        if(input_letter not in secretWord):
            lettersGuessed.append(input_letter)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, input_letter))
            guess_time -= 1


        if(input_letter in secretWord):
            lettersGuessed.append(input_letter)
            lettersGuessed_correct.append(input_letter)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed_correct))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman("y")
