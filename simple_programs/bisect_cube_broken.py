# bisect_cube.py 
# first only consider pos numbers
# Wont work for fractions initially

def bisect(cube, epsilon):
    cube = abs(cube)  # only considering positive numbers
    guess = (cube + 1) / 2
    guess_cubed = guess ** 3
    number_of_guesses = 0
    # sets the boundaries of the computation
    low = 1
    high = cube
    while abs(cube - guess_cubed) > epsilon:
        number_of_guesses += 1
        if number_of_guesses > 10:
            print("I am tired of this calculation")
            break
        if guess_cubed > cube:  # initial guess was too large
            high = guess # reduces to upper bound to the previous guess
            guess = (guess + low) / 2
        else:
            guess = (guess + cube) / 2   # this is Faulty!!!
        guess_cubed = guess ** 3 
        print(guess)
       
    print("There were %d number of guesses" %number_of_guesses) 

    if abs(cube - guess_cubed) <= epsilon:
        print(guess, "is a good approximation to", cube)
    else:
        print("No good approximation to", cube)
    return 

def test():
    bisect(27, 0.1)
    bisect(90, 1)

test()
