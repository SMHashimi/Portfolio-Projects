from turtle import *
import turtle as t
import random
tim = Turtle()
scren = Screen()
t.colormode(255)
angles_list = []
def heading():
    for int in range(1, 50, 3):
        number_of_circles = int
        angles_list.append(number_of_circles)
heading()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
tim.pensize(1)
angles = 0
for circle in range(72):
    angles += 5
    tim.speed("fastest")
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(angles)
scren.exitonclick()









