from asyncio import ALL_COMPLETED

from turtle_2_PlayerMovement import *
import random
cars_list = []
COLORS = ["red", "blue", "green", "yellow",
          "purple", "orange", "pink", "cyan", "magenta",
          "aqua", "lime", "maroon", "navy", "olive", "teal",
          "brown", "gray", "light pink", "light blue", "light green",
          "light yellow", "lavender", "peach puff", "light coral",
          "mint cream", "hot pink", "deep sky blue", "lime green",
          "gold", "crimson", "indigo", "coral", "firebrick"]

horizontal_position = [-210, -130, -50, 30, 110, 190, 270]
# car = Turtle("square")
# car.shapesize(stretch_wid = 1, stretch_len = 2)
# car.color(random.choice(COLORS))
speed = [-10, -20, -10, -25, -15, -13, -15]

def car_creation():
    for car_position in range(7):
        all_cars = Turtle("square")
        all_cars.penup()
        all_cars.color("black")
        all_cars.hideturtle()

        y_position = random.randint(-250, 280)
        all_cars.goto(x = 400, y = y_position)
        all_cars.showturtle()
        all_cars.color(random.choice(COLORS))

        all_cars.shapesize(stretch_len = 2, stretch_wid = 1)
        cars_list.append(all_cars)
        all_cars.forward(random.choice(speed))
        for car in cars_list:
            car.forward(random.choice(speed))