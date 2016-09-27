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

# Here's how
    # Recall that every path in the code must be hit
    # this means loops, conditionals, etc.

print(maxOfThree(10, 5, 3)) # first if is hit successfully, 2nd miss
print(maxOfThree(2, 1, 40)) # second if hit
print(maxOfThree(5, 20, 3)) # first if is missed, 2nd miss
print(maxOfThree(1, 10, 20)) # second if hit 

print('-' * 10)
print(10)
print(40)
print(20)
print(20)
