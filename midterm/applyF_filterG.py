
def f(i):
    return i + 2

def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    '''
    Assumes L is a list of integers.
    Assume function f and g are defined elsewhere.
    f takes in an integer, applies a function, returns another integer.
    g takes in an integer, applies a Boolean funcion, 
       returns either True or False
    Mutate L such that, for each element i originally in L, L contains
       i if g(f(i)) returns True and no other elements
    Returns the largest element in the mutated L or -1 if list is empty
    '''
    remove_these = [] # mutating a list while iterating over it requires this
    for i in L:
        if not g(f(i)):
            remove_these.append(i)

    for be_gone in remove_these:
        L.remove(be_gone)

    if L:
        return max(L)
    else:
        return -1


def tests():
    l = [0, -10, 5, 6, -4]
    print(applyF_filterG(l, f, g))
    print(l)

tests()
