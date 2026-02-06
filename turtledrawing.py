"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue") 


t = turtle.Turtle()
t.hideturtle() # Hide the turtle

t.color("red")
t.penup()
t.goto(-100, -100)
t.pendown()
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)

t.color("black")
t.penup()
t.goto(-120, 50)
t.pendown()
t.goto(0, 130)
t.goto(120,50)
t.goto(-120, 50)

t.color("blue")
t.penup()
t.goto(-25, -100)
t.pendown()
t.left(180)
t.forward(70)
t.left(90)
t.forward(50)
t.left(90)
t.forward(70)
t.left(90)
t.forward(50)

t.color("green")
t.penup()
t.goto(20, -30)
t.pendown()
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)


