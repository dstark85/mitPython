# write a program that prints the longest substring in 
#  a string that is in alphabetical order. 

# NOTES Save pos of first index and also the length of substr
#      - loop only to len - 2

# addendum: I should have consulted that 'aaa' is in order
s = 'teststring'

def long_alpha(s):
    saved_index = 0
    count = 1
    longest = 0
    new_index = 0
    for i in range(len(s) - 1):   # only loop to second to last char
        if s[i] <= s[i+1]:   # check alphabetical order
            count += 1
        else:
            if count > longest:   # update count when larger than longest
                longest = count
                saved_index = new_index   # save the index of long string
            count = 1
            new_index = i + 1
    if count > longest:
        return s[new_index:]
    return s[saved_index: saved_index + longest]


# deleted the git commit line from github
