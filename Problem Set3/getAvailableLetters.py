lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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

print(getAvailableLetters(lettersGuessed))