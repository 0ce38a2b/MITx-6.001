'''
Write an iterative function, gcdIter(a, b), that implements this idea.
One easy way to do this is to begin with a test value equal to the smaller of the two input arguments,
and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if(a > b):
        test_value = b
    else:
        test_value = a

    while(test_value > 0 ):
        if((a % test_value == 0) and (b % test_value == 0)):
            gcd = test_value
            break
        test_value -= 1

    return gcd

print(gcdIter(9,12))