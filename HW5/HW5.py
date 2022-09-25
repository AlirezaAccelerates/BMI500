# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:48:27 2022

@author: Alireza
"""

### ........................ Problem #1 ........................ ###


"""

Yes, there are more sophisticated types of dictionaries than the general dictionary. 
Looking at the data types section of the python standard library show these types.
More specifically, I found in following in the 'collections' section.
  -ChainMap: "is provided for quickly linking a number of mappings so they can be treated as 
              a single unit. It is often much faster than creating a new dictionary and running 
              multiple update() calls."
  -Counter: "is a dict subclass for counting hashable objects. It is a collection where elements 
              are stored as dictionary keys and their counts are stored as dictionary values."
  -OrderedDict: They are just like regular dictionaries but have some extra capabilities relating
                  to ordering operations."

What is a defaultDict: 
        A defaultdict works like an ordinary dict, but it is initialized with a function 
        of “default factory” that takes no arguments and provides the default value 
        for a nonexistent key. A defaultdict will never raise a KeyError as
        any nonexistent key t gets the value returned by the default factory. 
               
*Ref: https://docs.python.org/3/library/collections.html

"""

### ........................ Problem #2 ........................ ###

print("\nproblem #2 -- is this word palindrome?")


def Palindrome_check(word):
    
    """
A single word check to be a palindrome word.


Parameters:
    ----------
    word: str
        The word that a user wants to check.

Return: 
    ---------
    A booleanvariable:
        True: The word is palindrome.
        False: The word is palindrome.
    """

    if word == word[::-1]:
        print("The word '" + word + "' is a palindrome")
    else:
        print("The word '" + word + "' is not a palindrome")

# Providing examples for a palindrome and a non-palindrome word
print("\nAre rotator and apple palindrome?")
Palindrome_check("rotator")

Palindrome_check("apple")

### ........................ Problem #3 ........................ ###

print("\nproblem #2 -- Programming with strings\n")

s = ' The quick brown fox jumped over the lazy dog '
print('The input string (s) is: {}\n'.format(s) )


### Part A

print('Word <the> found at index {}\n'.format(s.find("the")))

print('Word <the> found at index {}\n'.format(s.rfind("the")))


### Part B

print('The output for dogs is {}\n'.format(s.index("dog")))

print('The output for dogs is {}\n'.format(s.rindex("dog")))

try:
    print('The output for dogs is {}\n'.format(s.index("cat")))
except:
    print('ValueError: The word <cat> not found')
    
try:
    print('The output for dogs is {}\n'.format(s.rindex("cat")))
except:
    print('ValueError: The word <cat> not found')

    
    

###------- PART C

print(s.split())
# ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

print("$$".join(s.split()))
# The$$quick$$brown$$fox$$jumped$$over$$the$$lazy$$dog


###------- PART D

print(s.lower())
#  the quick brown fox jumped over the lazy dog

print(s.upper())
#  THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG

print(s.title())
#  The Quick Brown Fox Jumped Over The Lazy Dog


###------- PART E

print(s.strip())
# The quick brown fox jumped over the lazy dog

# The strip function removes the spaces at the beginning and the end of s.


###------- PART F

print(s.replace("jumped", "flew"))
#  The quick brown fox flew over the lazy dog