# a simple number guessing program

# 0 - 100 (exclusive)

def quick_log(base, n):
    ''' Rounds up '''
    count = 0
    while n > 1:
        count += 1
        n //= base
    return count

def guess_number():
    print("Think of a number between 0 and 100!")
    prompt = '''Enter 'h' to indicate the guess is too high. 
                Enter 'l' to indicate the guess is too low.
                Enter 'c' to indicate I guessed correctly
             ''' 
    acceptable_responses = 'hlc'
    low = 0
    high = 100
    g = (low + high) // 2
    guess_attempts = 0
    attempts_needed = quick_log(2, 100) 

    while True:
        print("Is your secret number " + str(g) + '?')
        response = input(prompt)
        guess_attempts += 1
        
        if guess_attempts > attempts_needed:   # Beware of cheaters!
            print("LIAR!!")
            break

        while response[0] not in acceptable_responses:  # user better cooperate
            print("I don't recognize what you entered.")
            response = input(prompt)
        if response[0] == 'h':
            high = g
        elif response[0] == 'l':
            low = g
        else:
            print("Game over. Your secret number was: " + str(g))
            return g
        g = (low + high) // 2

            
guess_number()
