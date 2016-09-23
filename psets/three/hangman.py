# hangman.py
from random import choice

# a program that plays hangman

def hangman():
    '''
    An interactive session of hangman
    '''
    def get_word_list(f):
        '''
        gets a word list from file f. 
        returns the list of words
        '''
        # bring in from another file ('words.txt')
        f_hand = open(f)
        word_list = []
        for line in f_hand:
            word = line.strip() # get rid of whitespace
            if word.isalpha():   # ensure that no punctuation and that is > 1c 
                word = word.lower()  # lowercase everything
                word_list.append(word)

        return word_list
    def choose_word(word_list):
        '''
        Randomly choose a word from the list of words
        '''
        return choice(word_list)

    def print_message():
        print("Are you ready to play Hangman?")
        print("You have 8 lives")
        print("The entire word or individual letters may be guessed.")

    def make_dict(word):
        '''
        Accepts a string. Iterates through it, building a dict and initializing
        each letter key to value False
        False represents the fact that the letter hasn't been guessed.
        '''
        d = {}
        for letter in word:
            d[letter] = False
        return d

    def show_word(word, letter_dict):
        '''
        Accepts word string and letter dictionary. 
        Builds a string up based on whether the letters have been guessed
        Returns that string
        '''

        res = ''
        for letter in word:
            if letter_dict[letter]:
                res += letter
            else:
                res += '-'
        print(res)
   
    def get_guess():
        '''
        returns the guess that the user makes
        '''
        guess = input('what is your guess: ')
        return guess 

    def process_guess(guess, word, letter_dict):
        '''
        guess is a string of length 1 (a letter) or word guess
        word is a string of the word
        returns true when the guess is the same as the word, false otherwise
        
        ''' 
        def check_letter(letter, d):
            '''
            accepts letter as a one-char length string.
            d is a dictionary with one-char length strings as keys
            mutates d based on whether letter is in it or not
            '''
            if letter in d.keys():
                if d[letter]:
                    print("You already guessed this letter!")
                    # increment guesses
                    return None
                d[letter] = True

        def check_word(guess_word, word):
            '''
            takes two strings. Prints msg if equal
            '''
            if guess_word == word:
                print("Congratulations!")
                # end game
                return True
            else:
                print("That is not the word")
 

        if not guess.isalpha():
            print("The word only contains alphabetical characters")
            return False
        
        if len(guess) == 1:
            check_letter(guess, letter_dict)   
        else:
            return check_word(guess, word)
            
        return False
        
    lives = 9
    word_list = get_word_list('words.txt')
    not_guessed_letters = list('abcdefghijklmnopqrstuvwxyz')
    word = choose_word(word_list) 
    letter_dict = make_dict(word)
    print_message()
    show_word(word, letter_dict)
    while lives > 0:
        guess = get_guess()    
        if process_guess(guess, word, letter_dict):
            break
        show_word(word, letter_dict)
        lives -= 1

    if lives == 0:
        print("Sorry, you have lost")
        print("The word was", word)

           
hangman()
