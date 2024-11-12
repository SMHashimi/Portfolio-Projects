from turtle_SnakeMove import *

from turtle import Turtle

score = 0
score_board = Turtle()
score_board.penup()
score_board.color("white")
score_board.goto(-250, 310)
score_board.hideturtle()
# score_board.write(f"Score: {score}", align = "center", font = ("aerial", 24, "normal"))

def collision_wall():
        score_board.goto(0,0)
        score_board.write("GAME OVER", align  = "center", font = "Courier")
        moving_snake = False

highscore_board = Turtle()
highscore_board.high_score = 0
highscore_board.penup()
highscore_board.color("white")
highscore_board.goto(200, 310)
highscore_board.hideturtle()


def reset():
        score = 0
        score_board.clear()
















