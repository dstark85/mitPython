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
   

 
