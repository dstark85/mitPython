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
        return numerator / denominator

    def perimeter(n, s):
        '''
        Helper function:
        Returns the perimeter of the polygon
        '''  
        return n * s

    return round(area(n, s) + perimeter(n, s), 4)

print(polysum(3, 10))
