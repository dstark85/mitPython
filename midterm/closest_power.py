
def closest_power(base, num):
    '''
    base: base of the expoenential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base ** exp is closest to num
    Note that the base ** exp may either be greater or less than num
    In case of a tie, return the smaller value
    Returns the exponent.
    '''
    exp = 0
    while (base ** exp) <= num:
        diff = num - (base ** exp)
        exp += 1

    newDiff =  (base ** exp) - num

    if newDiff < diff:
        return exp
    else:
        return exp -1


def tests():
    print(closest_power(9, 1), "0") 
    print(closest_power(3, 12), "2")
    print(closest_power(2, 6), "2")
    print(closest_power(10, 80), "2")
    print(closest_power(7, 290), "3")

tests()

        
