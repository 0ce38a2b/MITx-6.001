secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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



print(getGuessedWord(secretWord, lettersGuessed))

