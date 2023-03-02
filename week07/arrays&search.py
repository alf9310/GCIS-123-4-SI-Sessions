"""
Session 7A: Arrays, Random & Linear Search Coding Activity.
@author: Audrey Fuller
@author: 
"""

import arrays
import time

'''
Make an array with even numbers from start to end
Parameters:
    :param int start: beginning of the array
    :param int end: ending of the array
'''
def make_even_array(start, end):
    return


'''
Find the first duplicate element in a given array of integers. 
Return -1 If there are no such elements.
Parameters:
    :param int array: the array of ints
Return:
    first duplicate
'''
def find_first_duplicate(array):
    store = ""
    no_dup = -1
    for number in range(len(array)):
        if str(array[number]) in store:
            return array[number]
        else:
            store += str(array[number])
    return no_dup

'''
Replaces characters in an array.
Parameters:
    :param int array: the array of ints
    :param int new: new character
    :param int end: old character to replace
'''
def replace_array(array, new, old):
    return

'''
Fill an array with random numbers using the passed in seed
Parameters:
    :param int size: size of the array
    :param int seed: seed for random
'''
def random_array(size, seed):
    return

'''
Search an array for the specified value using the linear search in an array
Parameters:
:param int array: array to be searched
:param int n: the value to be found
'''
def linear_search(array, n):
    return


def main():
    array = [100, 95, 50, 6, 1000]
    print(find_first_duplicate(array))

if __name__ == '__main__':
    main()