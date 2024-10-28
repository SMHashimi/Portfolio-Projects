from turtle_1PondScreenSetting import *

screen.tracer(0)
paddle = Turtle("square")
def paddle_creation_to_the_right_side(color):
    paddle.color(color)
    paddle.shapesize(stretch_len = 1, stretch_wid = 5)
    paddle.penup()
    paddle.goto(350, 0)

paddle_creation_to_the_right_side("white")




















