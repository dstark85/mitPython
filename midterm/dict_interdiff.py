
'''
  Assume you are given two dictionaries d1 and d2, each with integer keys and int values.
  You are also given a function f that takes two ints and performs an unknown operation
  on them and returns a value.

  Write dict_interdiff that takes the two dictionaries. The function returns a tuple of 
  two dictionaries: a dictionary of the intersection and a dictionary of the difference

  Intersect: the keys to the intersect are the keys that are commom in both d1 and d2.
  To get the values of the intersect dictionary, look at common keys in d1 and d2 and 
  apply the function f to these keys' values. d1 value is first parameter. d2 value is 
  second parameter. f is a dummy function. It's implementation is not important.

  Difference: a key-value pair in the difference dictionary is (a) every key-value pair
  in d1 whose key only appears in d1 and not in d2 or (b) every key-value pair in d2 whos
  key only appears in d2 and not d1.
  '''

def f(num1, num2):
    return num1 > num2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts of int keys and int values
    Returns a tuple of dicts that have intersection and difference
    '''
    intersection = {}
    difference = {}

    for key in d1: # loop over the first dictionary
        if key in d2.keys():  # check if it should be in intersection
            new_value = f(d1[key], d2[key])
            intersection[key] = new_value
        else:
            difference[key] = d1[key]  # Add the key-value to difference dict
            
    for key in d2:  # loop over second dictionary
        if key not in d1.keys():  # all intersection key-values were grabbed already
            difference[key] = d2[key]

    return (intersection, difference)


def tests():
    dictA = {1: 30, 2: 20, 3: 30, 5: 80}
    dictB = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90} 

    print(dict_interdiff(dictA, dictB))

    dictC = {1: 30, 2: 20, 3: 30}
    dictD = {1: 40, 2: 50, 3: 60}

    print(dict_interdiff(dictC, dictD))

tests()
