from turtle_2PongPaddleCreation import *

def paddle_up():
    #the x-axis does not change
    y_movement = paddle.ycor() + 15
    paddle.goto(paddle.xcor(), y_movement)
    print(y_movement)

def paddle_down():
    #the x-axis does not change
    y_movement = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_movement)
    print(y_movement)

screen.listen()
screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()













