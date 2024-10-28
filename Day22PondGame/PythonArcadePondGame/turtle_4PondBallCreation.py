from turtle_3PondPaddleMoving import *

ball = Turtle()

ball.shape("circle")
ball.color("white")

def ball_move():
     x_movement = ball.xcor() + 5
     y_movement = ball.ycor() + 5
     ball.penup()
     ball.goto(x_movement, y_movement)
# ball_move()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball_move()

screen.exitonclick()
