from turtle_3PondPaddleMoving import *

ball = Turtle()
ball.shape("circle")
ball.color("white")

# def ball_move():
#      x_movement = ball.xcor() + 10
#      y_movement = ball.ycor() + 10
#      ball.penup()
#      ball.goto(x_movement, y_movement)
#ball_move()

x_move = 10
y_move = 10

def ball_move():
     global x_move, y_move
     ball.penup()
     ball.goto(ball.xcor() + x_move, ball.ycor() + y_move)
     if ball.ycor() > 290 or ball.ycor() < -290:
          y_move *= -1
     if ball.xcor() > 390 or ball.xcor() < -390:
          x_move *= -1



