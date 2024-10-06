image_5colors = [(220, 149, 107), (140, 119, 8), (73, 127, 125), (200, 254, 252), (14, 122, 175)] ##the first color was the background color
from turtle import *
import random
import turtle as t
t.colormode(255)
tim = Turtle()
scren = Screen()
def left():
    tim.setheading(90)
    tim.dot(20)
    tim.forward(50)
    tim.dot(20)
    tim.setheading(180)
for pace in range(0, 9):
    tim.color(random.choice(image_5colors))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
left()
for left in range(0, 9):
    tim.color(random.choice(image_5colors))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    tim.dot(20)
tim.setheading(90)
tim.forward(50)
tim.setheading(0)
tim.dot(20)
tim.penup()
tim.dot(20)
for pace in range(0, 9):
    tim.color(random.choice(image_5colors))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
tim.dot(20)
scren.exitonclick()