from turtle import *

screen = Screen()
player = Turtle()

screen.bgcolor("white")
screen.setup(width = 700, height = 700)
screen.title("The TurtleCrossing by SayedMubarisHashimi")

player.shape("turtle")
player.color("black")
player.penup()
player.goto(0, -320)
player.setheading(90)

