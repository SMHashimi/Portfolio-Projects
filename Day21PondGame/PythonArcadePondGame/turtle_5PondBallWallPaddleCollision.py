from turtle_4PondBallCreation import *

x_move = 10
y_move = 10

def ball_WallPaddleCollisionX_Y():

     global x_move, y_move
     ball.penup()
     ball.goto(ball.xcor() + x_move, ball.ycor() + y_move)
     if ball.ycor() > 290 or ball.ycor() < -290:
          y_move *= -1
     if ball.xcor() > 380:
          ball.goto(0, 0)
          x_move *= -1
     if ball.xcor() < -380:
          ball.goto(0, 0)
          x_move *= -1
     if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
          x_move *= -1




