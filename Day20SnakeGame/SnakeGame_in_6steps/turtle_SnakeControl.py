from turtle_SnakeBody import *

def up():
    if turtles_list[0].heading() != 270:
        turtles_list[0].setheading(90)
def down():
    if turtles_list[0].heading() != 90:
        turtles_list[0].setheading(270)
def left():
    if turtles_list[0].heading() != 0:
        turtles_list[0].setheading(180)
def right():
    if turtles_list[0].heading() != 180:
        turtles_list[0].setheading(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")




