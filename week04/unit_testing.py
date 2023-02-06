"""
Session 4A: Introducing Return statements, unit testing, running pytest
            code paths(nested functions), refactoring, conditionals
@author: Audrey Fuller (alf9310)
         (some functions adapted from Zoe Bingham)
"""

import random # For dice game
import turtle as t

# What should we name the test file? What do we import?

# What are the two characteristics of a good test?

# What are the three parts of a test?

def is_odd(n):
    '''
    Returns true if n is odd, false otherwise 
    Parameters:
        :param int n: number
    :return boolean
    '''
    if(n % 2 == 1):
        return True
    
    return False

def is_even(n):
    '''
    Returns true if n is even, false otherwise 
    Parameters:
        :param int n: number
    :return boolean
    '''
    pass

def my_max(n1, n2):
    '''
    Takes two numbers and returns the greater one
    Parameters:
        :param int n1: number 1
        :param int n2: number 2
    :return int
    '''
    pass

def my_max(n1, n2, n3):
    '''
    Takes three numbers and returns the greater one
    Parameters:
        :param int n1: number 1
        :param int n2: number 2
        :param int n2: number 3
    :return int
    '''
    pass

def av_three(n1, n2, n3):
    '''
    Takes three numbers and returns the average
    Parameters:
        :param float n1: number 1
        :param float n2: number 2
        :param float n3: number 3
    :return float
    '''
    pass

#start dice game
def dice_game():
    '''
    Simulates a die rolling game, where each player rolls die three times.
    Whoever gets the higher roll a larger number of times wins. 
    '''
    pass

def roll():
    '''
    Generate a random roll 1-6 for the player and return it
    :return int 
    '''
    pass

def roll_off(roll_1, roll_2):
    '''
    Print the rolls and check who got the higher roll
    Parameters:
        :param int roll_1: 
        :param int roll_2:
    :return int player that won
    '''
    #what function can we reuse here?
    pass

def who_won(round_1, round_2, round_3):
    '''
    Print the round wins and check who got more
    Parameters:
        :param int round_1: 
        :param int round_2:
        :param int round_3:
    :return int player that won
    '''
    #what function can we reuse here?
    pass


def draw_circle(x, y, pen_color, fill_color, radius):
    t.penup()
    t.goto(x,y)
    t.pencolor(pen_color)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.goto(x,y)

def car_tire(x, y, size):
    radius1 = size # Big Circle radius
    radius2 = size/4 # Small Circle radius
    draw_circle(x,y, "black", "gray", radius1)
    draw_circle(x, y + radius1 - radius2, "black", "black", radius2)

def main():
    car_tire(0, 0, 100)
    car_tire(100, -100, 50)
    input()

main()