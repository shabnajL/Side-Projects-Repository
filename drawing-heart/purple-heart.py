import math
from turtle import *
## sine(n) -> to control the side-to-side movement (x-coordinate),
## cosine(n) -> to control the up-and-down movement of the pen (y-coordinate).


def heart_width(n):
    return (15*math.sin(n)**3)

    ## generates the x-coordinate for points on the heart using the sine function. 
    ## the cubing operation creates the characteristic indentation on the left side of the heart. 
    ## and the scaling factor of 15 influences the overall width of the heart.
    
    

def heart_shooting_length(n):
    return (10*math.cos(n) - 5*math.cos(2*n) - 2*math.cos(3*n) - math.cos(4*n))

    # [12*math.cos(n)] forms the primary curve of the heart.
    # [-5*math.cos(2*n)] creates a dip in the heart's curve.
    # [-2*math.cos(3*n)] further refines the shape of the heart's curve.
    # [-math.cos(4*n)] adds a final adjustment to the heart's curve.


speed(19000)
bgcolor("silver")
#bgcolor("black")
pensize(10)  # Set pensize to 5 before drawing the heart

for i in range(400):
    goto(heart_width(i)*20, heart_shooting_length(i)*20)
    for j in range(5):
        color("purple")
        #color("red")
    goto(0, 0)
    #print(i)
done()
