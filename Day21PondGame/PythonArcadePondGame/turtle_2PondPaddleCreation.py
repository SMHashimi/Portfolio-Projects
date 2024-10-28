from turtle_1PondScreenSetting import *

right_paddle = Turtle("square")
left_paddle = Turtle("square")

def right_paddle_creation_to_the_right_side(color):
    right_paddle.color(color)
    right_paddle.shapesize(stretch_len = 1, stretch_wid = 5)
    right_paddle.penup()
    right_paddle.goto(350, 0)
def left_paddle_creation_to_the_right_side(color):
    left_paddle.color(color)
    left_paddle.shapesize(stretch_len = 1, stretch_wid = 5)
    left_paddle.penup()
    left_paddle.goto(-350, 0)

right_paddle_creation_to_the_right_side("white")
left_paddle_creation_to_the_right_side("white")



















