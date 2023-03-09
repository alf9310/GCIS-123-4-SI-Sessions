"""
Session 8B & Bonus: Practical Review #2
                    Unit 4: Conditionals, Strings & Loops
                    Unit 5: Files & Exception Handling
                    Unit 6: Arrays, Recursion & Searching
@author: Audrey Fuller
"""

import arrays

'''
Print out all the values of an array in order.

Parameters:
    :param int array: input array
'''
def printArray(array):
    return


'''
Add every number in the file to some array. If the file contains a value that 
is not castable to an int throw a TypeError with the message 
"<thing> is not an int".
(note - thing.isdigit() will determine if a string can be an int or not)

Parameters:
    :param String filename: File full of numbers seperated by commas
Return:    
    :return: array of numbers from file
'''
def getNumbers(filename):
    return


'''
Do a recursive quicksort, but in reverse (greatest -> least)

Parameters:
    :param int array: input array
Return: 
    :return: sorted array from greatest to least
'''
def rev_quicksort(array):
    return

'''
Continously prompt user to input a file name.
If the prompt recieves "quit" then stop running. 
Call getNumbers to get the numbers in a file into an array. 
If a file does not exist, print "NO! Please enter a valid filename."
If it does print the original array using the 'print array' function.
Reverse quicksort the array using the 'rev_quicksort' function.
Print the reverse sorted array.
'''
def main():
    return

if __name__ == '__main__':
    main()