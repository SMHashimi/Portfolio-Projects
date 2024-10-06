from turtle import *
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(20)
screen.listen()
screen.onkey(key = "f", fun = move_forward)
screen.exitonclick()

