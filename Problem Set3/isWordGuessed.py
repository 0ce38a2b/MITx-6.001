secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

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

print(isWordGuessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))