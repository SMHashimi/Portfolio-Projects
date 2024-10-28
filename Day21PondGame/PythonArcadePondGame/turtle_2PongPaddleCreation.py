from turtle_1PondScreenSetting import *

screen.tracer(0)
right_paddle = Turtle("square")
def right_paddle_creation_to_the_right_side(color):
    right_paddle.color(color)
    right_paddle.shapesize(stretch_len = 1, stretch_wid = 5)
    right_paddle.penup()
    right_paddle.goto(350, 0)

right_paddle_creation_to_the_right_side("white")




















