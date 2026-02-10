"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
import turtle
turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)
tess.hideturtle()

for jas in range (0,255,10):
    tess.forward(10)
    tess.pensize(jas)
    tess.color(jas, 0, jas)  