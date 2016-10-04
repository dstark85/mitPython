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
    copy_list = []

      # checking for base case. When list is down to one element.  
    if len(aList) == 1: 
       if type(aList[0]) == type([]): # this list can contain other lists
           return copy_list + flatten( 
           pass # recurse here 
       else:
           return copy_list + aList[0]
    else:
        if type(aList[0]) == type([]):
            return copy_list 
            pass # recurse
        else: 
            return copy_list + aList[0]  # can return the value since it's not a list


def test():
    l1 = [1, 2, [3, 4], 'str']
    l_flat = flatten(l1)
    print(l1)
    print('>' * 10)
    print(l_flat)
    print('-' * 20)
    


test()
