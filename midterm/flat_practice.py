l = [1, 2, 3, 'str']
nestListOfOne = [ [1, 2, 'str'] ]
twoNestList = [ [1, 2, 'str'], [4, 5, 'foo'] ]
n1 = [ [1, 2, 3], 'str', [ ['abc', 'zzz', 10], 100], 99, ]

one_item_list = [3]
one_item_nest_list = [ [1, 2, 3] ]
multiple_item_list = [23, 4, 1, 'foo', 'str']
nest_list_on_second = [2, ['foo', 'str', 20], 2]

def flatMe(l):
    if len(l) < 1: # deals with an empty list
        return
    elif len(l) == 1:
        if type(l[0]) == type([]):
            # it's a list
            return flatMe(l[0])         
        else:
            # it's not a list
            return [l[0]]
    else:
        if type(l[0]) == type([]):
            # It's a list. Not the last one ...
            return flatMe(l[0]) + flatMe(l[1:])
        else:
            # not a list. Need to cast the element to list type
            return [l[0]] + flatMe(l[1:])


#print(flatMe(l))
#print(flatMe(nestListOfOne))
#print(flatMe(twoNestList))
#print(flatMe(nestsEverwhereList))
print(flatMe(one_item_nest_list))
print(nest_list_on_second)
print(flatMe(nest_list_on_second))
print(flatMe(n1))
print('<' * 20)
print(n1)
