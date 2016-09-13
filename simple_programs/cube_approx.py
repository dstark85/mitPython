# This program exhaustively checks solutions until one is good enough

def cube_approx(cube, epsilon, increment):
    ''' Assume a positive cube for now '''
    number_of_guesses = 0
    guess = 0.0
    neg_flag = False
    if cube < 0:
        cube = - cube 
        neg_flag = True

    while cube - guess ** 3 > epsilon:
        guess += increment
        number_of_guesses += 1 

    if neg_flag:
        guess = - guess
        cube = - cube    
    print(guess, 'is an approximation to', cube)
    print("The program took " + str(number_of_guesses) + " guesses.")
    return      


''' Tests '''
cube_approx(-27, 0.01, 0.0001)
cube_approx(27, 0.01, 0.0001)
cube_approx(28, 0.01, 0.0001)
cube_approx(-28, 0.01, 0.0001)

