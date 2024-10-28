from turtle import *
import random
tim = Turtle()
scren = Screen()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(5)
tim.speed("slowest")
direction = [0, 90, 180, 270]
for move in range(0, 300):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(direction))
scren.exitonclick()









