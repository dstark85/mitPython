# This program exhaustively checks solutions until one is good enough

def cube_approx(cube, epsilon, increment):
    ''' Assume a positive cube for now '''
    number_of_guesses = 0
    guess = 0.0
    neg_flag = False
    if cube < 0:  # changes cube to positive so that while loop is unaffected.
        cube = - cube 
        neg_flag = True

    while cube - guess ** 3 > epsilon:  # there is an error here!
        guess += increment
        number_of_guesses += 1 

    if neg_flag:
        guess = - guess
        cube = - cube    
    if abs(cube - guess ** 3) <= epsilon:
        print(guess, 'is an approximation to the cube root of', cube)
        print("The program took " + str(number_of_guesses) + " guesses.")
    else:
        print("No acceptable approximation was reached.")    
    return      


''' Tests '''
cube_approx(-27, 0.01, 0.0001)
cube_approx(27, 0.01, 0.0001)
cube_approx(28, 0.01, 0.0001)
cube_approx(-28, 0.01, 0.0001)

print ("test with smaller increment to make the program faster")
cube_approx(31, 0.0001, .1)
