from turtle import *

bgcolor("black")
speed(0)
hideturtle()

for i in range(150):
    color("blue")
    circle(i)
    color("indigo")
    circle(i*1.0)
    right(4)
    forward(4)
i = 150    
while i>0:
    color("chocolate")
    circle(i)
    color("orchid")
    circle(i*1.0)
    forward(4)
    right(4)
    i = i - 1


done()
