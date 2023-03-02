"""
Session 7B: Recursion
@author: Audrey Fuller
"""

import arrays
import time

'''
Find the base ^ exponent
Parameters:
    :param int base:
    :param int exponent:
'''
def exponent(base, exp):
    #base case?
    if exp == 0:
        print('Base Case')
        return 1
    #recursive case?
    else: 
        print("base " + str(base) + "   exponent: " + str(exp))
        return base * exponent(base, exp - 1)

'''
Recursive function to reverse the words in a string
Parameters:
    :param String string:
    :param int index:
'''
def reverse_string(string, index = 0):
   reverse_str = ""
   words = string.split()
   if len(words) == index: # Base case
       return ""
   else: # Recursive case
       reverse_str += reverse_string(string, index + 1) + words[index] + " "
   return reverse_str


def main():
    #array = [1, 2, 4, 6, 6, 8, 10, 11, 11]
    print(exponent(6, 10))
    #string = "hello world!"
    #print(string)
    #print(reverse_string(string))

if __name__ == '__main__':
    main()