# with map instead
def dotProduct(listA, listB):
    '''
    listA: a list of ints
    listB: a list of ints 
    lists have same number of elements
    return the dot product of the lists
    '''
    def multiply(a, b):
        return a * b

    res = 0
    for product in map(multiply, listA, listB):
        res += product

    return res


def tests():
    print(dotProduct([1,2,3], [1,2,3]), "22")
    print(dotProduct([2, 4], [1, 3]), "14")
    print(dotProduct([1], [2]), "2")


tests()
