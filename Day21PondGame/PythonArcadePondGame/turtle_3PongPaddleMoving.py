from turtle_2PongPaddleCreation import *

def right_paddle_up():
    #the x-axis does not change
    y_movement = right_paddle.ycor() + 15
    right_paddle.goto(right_paddle.xcor(), y_movement)
    print(y_movement)

def right_paddle_down():
    #the x-axis does not change
    y_movement = right_paddle.ycor() - 20
    right_paddle.goto(right_paddle.xcor(), y_movement)
    print(y_movement)

screen.listen()
screen.onkey(right_paddle_up, "Up")
screen.onkey(right_paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()













