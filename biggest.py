animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

'''
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'
'''


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    length_list = []
    for value in aDict.values():
        length_list.append(len(value))

    longest = max(length_list)

    for key in aDict.keys():
       if(len(aDict[key]) == longest):
           return key

print(biggest(animals))
