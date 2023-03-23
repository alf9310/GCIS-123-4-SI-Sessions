"""
Session 9B: Lists & Tuples Answers
@author: Audrey Fuller
"""

'''
Write a Python program to get a list, sorted in increasing order by the last 
element in each tuple from a given list of non-empty tuples.

Parameters:
    :param List(tuple) tuples: list of tuples
Return:    
    :return: list of tuples sorted by last element
'''
def sort_list_last(tuples):
    for i in range(1, len(tuples)):
        t_last = tuples[i][len(tuples[i]) - 1]
        while(t_last < tuples[i - 1][len(tuples[i]) - 1] and i > 0):
                temp = tuples[i - 1]
                tuples[i - 1] = tuples[i]
                tuples[i] = temp
                i -= 1
    return tuples

'''Optional other solution using built-in sort'''
def last(n): return n[len(n) -1]

def sort_list_last_key(tuples):
  return sorted(tuples, key=last)

def main():
    tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_last(tuples))
    print(sort_list_last_key(tuples))

if __name__ == '__main__':
    main()