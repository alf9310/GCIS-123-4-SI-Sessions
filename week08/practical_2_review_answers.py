"""
Session 8B & Bonus: Practical Review #2 ANSWERS
@author: Audrey Fuller
"""

import arrays

def printArray(array):
    for index in range(len(array) - 1):
        print(str(array[index]) + ", ", end = '')
    print(array[len(array) - 1]) 


def getNumbers(filename):
    array = []
    with open(filename) as file:
        for line in file:
            for num in line.strip().split(", "):
                if(num.isdigit()):
                    array.append(int(num))
                else:
                    raise TypeError(num + " is not an int.")
    return array


def rev_quicksort(array):
    if(len(array) == 1 or len(array) == 0):
        return array
    else:
        less = []
        equal = []
        greater = []
        pivot = array[0]
        for num in range(len(array)):
            if(array[num] < pivot):
                less.append(array[num])
            elif(array[num] > pivot):
                greater.append(array[num])
            else:
                equal.append(array[num])
        result = []
        result += (rev_quicksort(greater))
        result += (equal)
        result += (rev_quicksort(less))
        return result


def main():
    while(True):
        filename = input("file name: ") # Reading file
        if(filename == "quit"):
            break
        array = []
        try:
            array = getNumbers(filename)
        except FileNotFoundError:
            print("File DNE")
        
        # Print array, sort and print again
        printArray(array)
        sortedArray = rev_quicksort(array)
        print("Sorted array: ")
        printArray(sortedArray) 


if __name__ == '__main__':
    main()