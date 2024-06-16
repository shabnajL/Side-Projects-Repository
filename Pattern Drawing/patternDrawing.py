from turtle import *

bgcolor("black")
speed(0)
hideturtle()
colors=['red','purple','green','orange','orchid','yellow']

    
for i in range(150):
    color("blue")
    circle(i)
    color(colors[i%6])
    #color("indigo")
    circle(i*1.0)
    width(i/100+1)
    forward(i)
    left(59)
    #right(4)
    #forward(4)
i = 89    
while i>0:
    color("chocolate")
    circle(i)
    color("blue")
    circle(i*1.0)
    forward(4)
    right(4)
    i = i - 1


done()
