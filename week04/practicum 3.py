


import turtle as t
import math

def draw_square(pen_color, fill_color, length):
    t.penup()
    t.pencolor(pen_color)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.end_fill()
    t.penup()
    t.forward(length/2)
    t.right(90)
    t.right(45)

def draw_squares(size):
    t.speed(40)
    t.goto(-size/2, -size/2)
    draw_square('black', 'red', size)
    draw_square('black', 'orange', size/math.sqrt(2))
    draw_square('black', 'yellow', size/2)
    draw_square('black', 'green', size/(2* math.sqrt(2)))
    draw_square('black', 'blue', size/ 4)
    draw_square('black', 'purple', size/ (4 * math.sqrt(2)))

def main():
    draw_squares(300)
    input()

main()