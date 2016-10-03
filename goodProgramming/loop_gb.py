

def foo(x, a):
    '''
    x: a positive integer argument
    a: a positive integer argument
   
    returns an integer
    '''

    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


# Here's how: 
  # with loops, examine: no entrances, 1 entrance and many entrances

# case1: no loop entrance
print(foo(1, 2)) # returns 0

# case2: one loop entrance
print(foo(11, 10)) # returns 1

# case3: many loops
print(foo(100, 2)) # returns 50
   
