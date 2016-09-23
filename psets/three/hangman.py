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


    word_list = get_word_list('words.txt')
    not_guessed_letters = list('abcdefghijklmnopqrstuvwxyz')
    word = choose_word(word_list) 
    letter_dict = make_dict(word)
    print_message()
    show_word(word, letter_dict)
    guess = get_guess()    


def get_guess():
    '''
    returns the guess that the user makes
    '''
    guess = input('what is your guess: ')
    return guess 

def check_letter(letter, possible_guesses):
    '''
    Take a letter and see if it has been guessed already.
    Return True if it is a new guess
    '''
    return letter in possible_guesses
            
hangman()
