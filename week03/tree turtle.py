"""
Week 3 Session B: Turtle activity to build farmiliarity with turtle by creating 
a scalable tree (such as the in-class example).

Concepts: Scope, Functions, Parameters, Incremental Developement, Turtle
@author: Audrey Fuller
"""

#In-class tree activity review
import turtle as t

def reset_turtle():
    t.tracer(False)
    t.penup()
    t.goto(0,0)
    t.speed(0)
    t.pencolor("black")

def triangle(x, y, size, pen, fill):
    t.goto(x, y)
    t.pencolor(pen)
    t.fillcolor(fill)
    t.begin_fill()
    t.pendown()
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.end_fill()
    reset_turtle()

def rectangle(x,y,width,height,pen,fill):
    t.goto(x, y)
    t.pencolor(pen)
    t.fillcolor(fill)
    t.begin_fill()
    t.pendown()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    reset_turtle()

def tree(x,y,size):
    t.penup()
    t.goto(x, y)
    rectangle(x,y,size/2,size*2,"brown","brown")
    triangle(x - size, y + size*2, size*2.5, "green", "green")
    triangle(x - size, y + size*3, size*2.5, "green", "green")
    reset_turtle()

def main():
    tree(-100,-300,100)
    input()

main()