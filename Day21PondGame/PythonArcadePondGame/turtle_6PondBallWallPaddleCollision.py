from turtle_5PondScoreBoard import *

x_move = 10
y_move = 10

def ball_WallPaddleCollisionX_Y():
     global x_move, y_move
     ball.penup()
     ball.goto(ball.xcor() + x_move, ball.ycor() + y_move)
     if ball.ycor() > 290 or ball.ycor() < -290:
          y_move *= -1
     if ball.xcor() > 380:
          score_board_l.l_score += 1
          score_board_l.clear()
          score_board_l.goto(-190, 225)
          score_board_l.write(score_board_l.l_score, align="center", font=("Courier", 50, "normal"))
          ball.goto(0, 0)
          x_move *= -1
     if ball.xcor() < -380:
          score_board_r.r_score += 1
          score_board_r.clear()
          score_board_r.goto(190, 225)
          score_board_r.write(score_board_r.r_score, align="center", font=("Courier", 50, "normal"))
          ball.goto(0, 0)
          x_move *= -1
     if ball.distance(right_paddle) < 50 and ball.xcor() > 325 or ball.distance(left_paddle) < 50 and ball.xcor() < -325:
          x_move *= -1




