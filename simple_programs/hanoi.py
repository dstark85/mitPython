# hanoi.py

# a recursive solution to the towers of hanoi problem

def printMove(fr, to):
    print("move from " + str(fr) + ' to ' + str(to))


def hanoi_recurse(n, fr, to, spare):
    '''
    If stack contains only one element, it can be moved. (Base Case)
    If stack contains more than one element, continue moving elements until base case
       hanoi_recurse(stack - 1, move)
    If know how to move a small stack, simple do that until the stack is actually 
      small. 
    Stack with 1 simply just moves
    Stack with 2 requires that the first is moved to an empty tower and then the
      larger is moved with the smaller following.
    Stack with 3: Do stack 2. Then stack 1 and stack 2 again. 
    '''
    if n == 1:
        printMove(fr, to)
    else:
        hanoi_recurse(n - 1, fr, spare, to)
        hanoi_recurse(1, fr, to, spare)
        hanoi_recurse(n - 1, spare, to, fr)
    

print(hanoi_recurse(4, 'P1', 'P2', 'P3')) 
    
    
    
