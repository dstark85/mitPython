def deep_reverse(L):
    ''' assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the ints in every element of L.
    It does not return anything
    '''
    for miniList in L:
        miniList.reverse()    

    L.reverse()


def tests():
    L1 = [ [1, 2, 3], [21, 32, 43], [28, 97, 31, 18] ]
    L2 = [ [1], [2, 1] ]
    L3 = [ [1, 2], [3, 4], [5, 6, 7] ]

    print(L1)
    deep_reverse(L1)
    print('-' * 20)
    print(L1)

    print(L2)
    deep_reverse(L2)
    print('-' * 20)
    print(L2)

    print(L3)
    deep_reverse(L3)
    print('-' * 20)
    print(L3)

tests()
