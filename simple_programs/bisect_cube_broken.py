# bisect_cube.py 
# first only consider pos numbers

def bisect(cube, epsilon):
    guess = (cube + 1) / 2
    cube = abs(cube)  # only considering positive numbers
    guess_cubed = guess ** 3
    number_of_guesses = 0
    while abs(cube - guess_cubed) > epsilon:
        number_of_guesses += 1
        if guess_cubed > cube:  # initial guess was too large
            guess = (guess + 1) / 2
        else:
            guess = (guess + cube) / 2
        guess_cubed = guess ** 3 
       
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
