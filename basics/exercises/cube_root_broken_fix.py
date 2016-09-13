# This Program by Eric Grimson can produce incorrect results
#  Exercise: Type in an input that produces an incorrect result.

def cube():
    x = int(input('Enter an integer: '))
    ans = 0
    while ans**3 < x:
        ans = ans + 1
    if ans ** 3 != x:
        print(str(x) + ' is not a perfect cube')
    else:
        print('Cube root of ' + str(x) + ' is ' + str(ans))
   

# This code only works on positive numbers. 
   # -8 is a perfect cube since -2 ** 3 = -8
   # however, the above code does not check negative numbers
   # Write new code that corrects this

def cube_right():
    pass 
