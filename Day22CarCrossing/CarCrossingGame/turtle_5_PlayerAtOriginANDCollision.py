from turtle_4_scoreboard import *

def back_at_origin():
    if player.ycor() > 300:
        score_board.score += 1
        score_board.clear()
        score_board.write(f"Level: {score_board.score}", align="center", font=("Courier", 25, "normal"))
        player.goto(0, -320)

def game_over():
    score_board.goto(0, 0)
    score_board.write(f"Game Over", align="center", font=("Courier", 25, "normal"))


