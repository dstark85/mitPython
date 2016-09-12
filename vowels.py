# s is a string of lowercase characters.

# Write a program to count the vowels in it. 
  # vowels are in the set: 'aeiou' 

def count_vowels(s):
    count = 0
    vowels = 'aeiou'
    for ch in s:
        if ch in vowels:
            count += 1 
    return count
