# Write a recursive Python function, given a non-negative integer N,
# to count and return the number of occurrences of the digit 7 in N.


def count7(N):
    if N < 10:
        if N % 10 == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return 1 + count7(N//10)
    else:
        return 0 + count7(N//10)


# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers.
# For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    pairwise_sum = 0
    for i in range(len(listA)):
        pairwise_sum += listA[i] * listB[i]
    return pairwise_sum

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    result_key = []

    for key_o in aDict.keys():
        num = 0
        for key_i in aDict.keys():
           if (aDict[key_o] == aDict[key_i]):
               num += 1
        if(num == 1):
            result_key.append(key_o)

    return result_key

print(uniqueValues({1: 1, 2: 1, 3: 1}))


def laceStringsRecur(s1, s2):
    '''
    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    :param s1: string
    :param s2: string
    :return: Interlaced strings
    '''
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            # If the first string is empty, append the second one to the output and STOP
            return out + s2
        if s2 == '':
            # If the first string is empty, append the second one to the output and STOP
            return out + s1
        else:
            # Append to the output the next character of each of the two strings
            # and recursively interlace the remaining sub-strings
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

print(laceStringsRecur("azzzzol", "mmmzzzzlop"))


def score(word, f):
    """
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
    letter_score_list = []
    word = word.lower()
    alphabet = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    for i in range(len(word)):
        letter_score = i * alphabet[word[i]]
        letter_score_list.append(letter_score)

    max1 = max(letter_score_list)
    letter_score_list.remove(max1)

    max2 = max(letter_score_list)

    return(f(max1,max2))


