from turtle_SnakeMove import *

from turtle import Turtle

score = 0
score_board = Turtle()

score_board.penup()
score_board.color("white")
score_board.goto(0, 310)
score_board.hideturtle()
# score_board.write(f"Score: {score}", align = "center", font = ("aerial", 24, "normal"))

def collision_wall():
        score_board.goto(0,0)
        score_board.write("GAME OVER", align  = "center", font = "Courier")
        moving_snake = False






















