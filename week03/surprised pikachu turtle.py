"""
Week 3 Session A: Turtle activity to build farmiliarity with turtle by creating 
a suprised pikachu drawing.

Concepts: Scope, Functions, Parameters, Incremental Developement, Turtle
@author: Audrey Fuller
Adapted from Zoe Bingham activity
"""

#Surprised Pikachu Outline 

# Import the library for turtle
import turtle as t

# Initialize a few global variables for a default color, location, turtle size, and pen size

# Initialize static global variables for the colors of pikachu

# Make a function to draw the base of a pikachu (Use given function below)
def draw_arc(degrees):
    for increment in range(180):
        t.forward(1)
        t.right(1)

# Make a function to draw the pikachu eyes

# Make a function to draw the pikachu nose

# Make a function to draw the pikachu cheek blush

# Make a function to draw the pikachu mouth

def triangle(x, y, width, height, pen, fill, offset):
    t.penup()
    t.goto(x, y)
    t.pencolor(pen)
    t.fillcolor(fill)
    t.begin_fill()
    t.pendown()
    t.forward(width)
    t.left(120-offset)
    t.forward(height)
    t.left(120+offset)
    t.forward(height)
    t.left(120)
    t.end_fill()

# Make a function that puts all of the elements of pikachu together with parameters for the x and y coords and size
def draw_pika(x, y, fill_color, pen_color, pen_size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(pen_size)
    t.left(90)
    draw_arc(180)
    triangle(20, 100, 50, 70, pen_color, fill_color, 0)

def circle(x, y, radius, pen_color, fill_color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def circles(x, y, radius, pen_color, fill_color):
    circle(x, y, radius, pen_color, fill_color)
    circle(x, y+radius+radius/2, radius/2, pen_color, fill_color)
    #circle(x, y, radius/4, pen_color, fill_color)


# Call our pikachu function multiple times in our main method 
def main():
    t.speed(10)
    #draw_pika(0,0, 'yellow', 'black', 3)
    circles(-100, -100, 100, 'black', 'cyan')
    input()

main()