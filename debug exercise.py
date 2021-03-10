def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        # rem(x-a, a) wrong
        return rem(x-a, a)

# print(rem(7, 5))


def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
       # return 0 wrong
        return 1
   else:
        return n * f(n-1)

print(f(0))