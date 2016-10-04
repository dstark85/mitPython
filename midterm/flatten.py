'''
   Write a function to flatten a list. The list contains other lists, string
   or ints. [ [1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5] is flattened to
   [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
'''
count = 0
def flatten(aList):
    '''
    aList: list
    Returns a copy of aList, which is a flattened version of aList
    '''
    global count
    count += 1 
    list_copy = []
    for element in aList:
        if type(element) == type([]):
            return (list_copy) += flatten(element)
        else:
            list_copy.append(element)
        
    return list_copy    

def test():
    l1 = [1, 2, [3, 4], 'str']
    l_flat = flatten(l1)
    print(l1)
    print('>' * 10)
    print(l_flat)
    print('-' * 20)
    


test()
