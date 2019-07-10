"""
The code below generates a given number of random strings that consists of numbers and
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import sys

def RandomStringGenerator(final_length=12, letter_lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    random_string = ''
    for i in range(final_length+1):
        random_string += random.choice(letter_lst)
    return random_string

def BatchStringGenerator(amount, mini=8, maxi=12):
    result = []
    for i in range(amount):
        final_length = None
        if mini < maxi:
            final_length = random.choice(range(mini, maxi))
        elif mini == maxi:
            final_length = mini
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        result.append(RandomStringGenerator(final_length))
    return result

mini = int(input('Enter minimum string length: '))
maxi = int(input('Enter maximum string length: '))
amount = int(input('How many random strings to generate? '))

print(BatchStringGenerator(amount, mini, maxi))
