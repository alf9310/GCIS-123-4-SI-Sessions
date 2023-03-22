"""
Session 9B: Lists & Tuples 
@author: Audrey Fuller
"""

'''
Write a Python program to get a list, sorted in increasing order by the last 
element in each tuple from a given list of non-empty tuples.
HINT: list[][] to access sequence inside of a sequence
ex) input:  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Parameters:
    :param List(tuple) tuples: list of tuples
Return:    
    :return: list of tuples sorted by last element
'''
def sort_list_last(tuples):
    return

def main():
    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_last(tuples))

if __name__ == '__main__':
    main()