import turtle
from random import randint
# from randomColor import * #randname
##


## Funtions

def equallines(size):
    t.backward(size)
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(size)


def dtriangle(size):
        t.down()
        for i in range(3):
            t.right(120)
            t.forward(size*2)
        t.up()

def filledCircle(size,color='blue'):
    t.fillcolor(color)
    t.down()
    t.begin_fill()
    t.right(size*20)
    t.circle(size)
    t.end_fill()
    t.up()


def filledSquare(size,color='blue'):
    t.fillcolor(color)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(size)
    t.end_fill()
    t.up()


# User Variables
screen_x = 400
screen_y = 401
size = randint(1,200)



# Turtle Setup
t=turtle.Pen()
t.shape()
t.reset()
screen = turtle.Screen()
screen.screensize(screen_x, screen_y)



## Begin Program -
#equallines(100)
#dtriangle(123)

#print(screen_x,' ',screen_y)

##equallines(size)
##t.backward(size)
##t.up()
##t.right(90)
##t.forward(20)
##t.left(90)
##t.down()
##t.forward(size)
##
##
##dtriangle(size)
##filledCircle(size)
##filledSquare(size)

# Start to dootle
for i in range(100):
    t.down()
    t.forward(1+i)
    t.right(i+i)



for i in range(12):
    color = randname()
    t.setpos(180+i,-.5*i)
    t.circle(40, 270)
    t.forward(90+i)
    filledSquare(i*8,color)
    t.forward(150-i)
    filledCircle(i*3,color)
    t.setpos(-180+i,-170-i)
    t.setheading(90+i)
    filledCircle(11*randint(2,7),color)


    
