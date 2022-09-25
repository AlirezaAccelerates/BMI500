"""
BMI 500 - Natural Language Processing
Alireza Rafiei - Fall 2022 - HW5
"""

### ........................ Problem #1 ........................ ###


"""

Yes, there are more sophisticated types of dictionaries than the general ones. 
The "data types" section of the "python standard library" provides information 
about these types. More specifically, I found the following in the 'collections' section.
  -ChainMap: "is provided for quickly linking a number of mappings so that they can be treated as 
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
A single word checks to be a palindrome word.


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
        print('The word ' + word + ' is a palindrome.')
    else:
        print('The word ' + word + ' is not a palindrome.')

# Providing examples for a palindrome and a non-palindrome word
print("\nAre <rotator> and <apple> palindrome?")
Palindrome_check("rotator")

Palindrome_check("apple")

### ........................ Problem #3 ........................ ###

print("\nproblem #3 -- Programming with strings")

s = ' The quick brown fox jumped over the lazy dog '
print('The input string (s) is: {}\n'.format(s) )


### Part A

print('Word <the> found at index {}'.format(s.find("the")))

print('Word <the> found at index {}\n'.format(s.rfind("the")))


### Part B

print('The output for dogs is {}'.format(s.index("dog")))

print('The output for dogs is {}'.format(s.rindex("dog")))

try:
    print('The output for cats is {}'.format(s.index("cat")))
except:
    print('ValueError: The word <cat> not found')
    
try:
    print('The output for cats is {}'.format(s.rindex("cat")))
except:
    print('ValueError: The word <cat> not found\n')

    
### Part C

print('The split of the string is: {}'.format(s.split()))

print('Join the string via the marker <$$> is: {}\n'.format("$$".join(s.split())))


### Part D

print('The outputs of the lower function is: {}'.format(s.lower()))

print('The outputs of the upper function is: {}'.format(s.upper()))

print('The outputs of the title function is: {}\n'.format(s.title()))


### Part E

print('The strip function eliminates the spaces at the beginning and the end of the string. Example:')

print(s.strip())


### Part E
print('\nReplacing <jumped> with <flew>')
print(s.replace("jumped", "flew"))

### ........................ Problem #4 ........................ ###

print("\nproblem #4 -- Generating frequency distributions\n")

### Part A
S_processed = s.lower().split()
print('The pre-processed string is: {}'.format(S_processed))


### Part B
from nltk.probability import FreqDist
dist_processed = FreqDist(S_processed)

### Part C
print('The distribution output of the preprocessed string is: {}'.format(dist_processed.items()))


### Part D

dist = FreqDist(s)
print('The distribution output of the orginal string is: {}\n'.format(dist.items()))

"""
Before applying the pre-processing steps, the provided string (s) is iterable.
Hence, the FreqDist function aims to find the frequency of each character. On the 
other  hand, after the pre-processing steps, a list of the words contained in the 
string (s) is iterable. Thus, the FreqDist function finds the frequency of each of 
these words.
"""





