from turtle import *
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(20)
def move_backwards():
    tim.backward(10)
def clockwise():
    tim.right(+15)
def counter_clockwise():
    tim.left(15)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forward, "w", )
screen.onkey(move_backwards, "s", )
screen.onkey(clockwise, "a", )
screen.onkey(counter_clockwise, "d", )
screen.onkey(clear, "c")
screen.exitonclick()