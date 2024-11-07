from turtle_4PondBallCreation import *

score_board_l = Turtle()
score_board_l.color("white")
score_board_l.penup()
score_board_l.hideturtle()
score_board_l.l_score = 0
score_board_l.goto(-190, 225)
score_board_l.write(score_board_l.l_score, align = "center", font = ("Courier",50, "normal"))

score_board_r = Turtle()
score_board_r.color("white")
score_board_r.penup()
score_board_r.hideturtle()
score_board_r.r_score = 0
score_board_r.goto(190, 225)
score_board_r.write(score_board_r.r_score, align = "center", font = ("Courier",50, "normal"))









