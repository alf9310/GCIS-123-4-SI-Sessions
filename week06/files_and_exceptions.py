"""
Session 6A: File Reading, error handling & exceptions activities.
@author: Audrey Fuller
@authod: Zoe Bingham (base printing code)
"""

def print_line_by_line(filename):
    '''
    Open a file and print each line. Between each line, print a '...'

    Parameters:
    :param string filename: the name of the file to be opened
    '''
    with open(filename) as file:
        for line in file:
            print(line.strip() + "...")
            print("...")



def print_character_by_character(filename):
    '''
    Open a file and print each line. Print each character in this format "(C)"
    
    Parameters:
    :param string filename: the name of the file to be opened
    '''

    pass

def print_word_by_word(filename):
    '''
    Open a file and print each line. Print each word in the file separated by a new line
    
    Parameters:
    :param string filename: the name of the file to be opened
    '''
    
    pass

def make_text_emoji(filename):
    '''
    Open a file and use each character to make an emoticon. Each line is an
    emoticon, in the format left_side, middle, right side. Print them out with 
    () between the middle
    
    Parameters:
    :param string filename: the name of the file to be opened'''
    
    pass

def main():
    file1 = "data/haiku.txt"
    file2 = "data/emoticons.csv"
    print_line_by_line(file1)
    print_character_by_character(file1)
    print_word_by_word(file1)
    make_text_emoji(file2)

    # For errors
    try:
        print_line_by_line(input("File Name: "))
        print_line_by_line("testing, testing?")
        print_line_by_line("ಠ_ಠ")
    except FileNotFoundError as FNF:
        print("Enter valid file name")

if __name__ == "__main__":
    main()