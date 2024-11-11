from turtle import *

screen = Screen()
player = Turtle()

screen.bgcolor("black")
screen.setup(width = 700, height = 700)
screen.title("The TurtleCrossing by SayedMubarisHashimi")
screen.tracer(0)

player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -320)
player.setheading(90)

game_is_on = True
