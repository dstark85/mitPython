# This is another interesting recursive solution

def union(set1, set2):
    '''
    set1 and set2 are collections of objects, each of which might be 
     empty.
    Each set has no duplicates within itself, but here may be objects
      that are in both sets. Objects are assumed to be of the same type.

    Returns one set containing all elements from both input sets, but 
     with no duplicates.
    '''
 
    if len(set1) == 0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:], set2)
    else:
        return set1[0] + union(set1[1:], set2)


# Here's how:

# case1: length of set 1 is in fact 0
print(union('', 'a'))

# case2: length of set1 is not 0. No shared elements
print(union('a', 'b'))

# case3: length of set1 is not 0. Shared elements
print(union('abc', 'bd'))

print('-' * 10)

print('a')
print('ab')
print('acbd')
  
