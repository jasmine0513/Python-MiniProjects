"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu	
"""
import turtle

t = turtle.Turtle()
t.speed(0)     # Set the turtle's speed to 0 (fastest)
t.pensize(2)   # Set the turtle's pen size to 2
t.hideturtle() # Hide the turtle


## TODO: implement the following pseudocode:
## Repeat 36 times: 
for jasmine in range(36):
## Repeat 3 times: 
  for jasmine in range(3):
## Change the color to pink.
    t.color("pink")
## Walk forward 80 steps.  
    t.forward(80)
## Turn right 60 degrees. 
    t.right(60)
## Change the color to red.
    t.color("red")
## Walk forward 80 steps. 
    t.forward(80) 
## Turn right 60 degrees.
    t.right(60)
## Turn right 10 degrees.
  t.right(10)
