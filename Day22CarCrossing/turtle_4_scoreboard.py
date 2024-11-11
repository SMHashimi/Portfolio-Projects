from turtle_3_CarsMoving import *

score_board = Turtle()
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.score = 1
score_board.goto(-258, 305)
score_board.write(f"Level: {score_board.score}", align = "center", font = ("Courier", 25, "normal"))
