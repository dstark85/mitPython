# a program that prints the sum of area and perimeter of a polynomial.

from math import *

def polysum(n, s):
    '''
    Takes two inputs: n is an int for number of sides. 
                      s is float for length
    Returns sum of area and perimeter of the polygon
    '''
    def area(n, s):
        '''
        Helper function:
        Returns the area of the polygon: 
        (0.25 * n * s^2 ) / (tan (pi / n))
        '''
        denominator = tan(pi / n)
        numerator = (0.25 * n * s ** 2) 
        print("Area is", numerator / denominator)
        return numerator / denominator

    def perimeter(n, s):
        '''
        Helper function:
        Returns the perimeter of the polygon
        '''  
        return n * s

    ans = area(n, s) + perimeter(n, s) ** 2
    return round(ans, 4)


# test cases are irrevelant after proof-reading the question
'''
print("Triangle with side length 10")
print("Perimeter = 30")
print("Area = 10 * 5 sqroot 3")
print(10 * 5 * sqrt(3))
print('-------')
print(polysum(3, 10))

print("Square with side 10")
print("Perimeter = 40")
print("Area = 100")
print(polysum(4, 10))
'''
print(polysum(4, 74))
