from turtle_1_PlayerANDScreenConfiguration import *

# print(player.ycor())
# print(player.xcor())

def go_up():
    #the x-axis does not change
    y_move = player.ycor() + 10
    player.goto(player.xcor(), y_move)
screen.listen()
screen.onkey(go_up, "w")


