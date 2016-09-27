def maxOfThree(a, b, c):
    '''
    a, b, and c are nums
    returns: the maximum value
    '''

    if a > b:
        bigger = a
    else:
        bigger = b

    if c > bigger:
        bigger = c 

    return bigger


# how can this function be tested using glass box testing?
