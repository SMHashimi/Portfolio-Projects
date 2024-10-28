from turtle import *

screen = Screen()
screen.bgcolor("black")
screen.title("The Nokia 3310 Snake Game")
screen.setup(700, 700)

# turtle_1 = Turtle("square")
# turtle_1.color("white")

# turtle_2 = Turtle("square")
# turtle_2.color("white")
# turtle_2.goto(-20, 0)

# turtle_3 = Turtle("square")
# turtle_3.color("white")
# turtle_3.goto(-40, 0)

snake_moves = [(0, 10), (-20, 10), (-40, 10)]
turtles_list = []
# def snake_body(shape, color):
#     for move in snake_moves:
#         new_turtle = Turtle(shape)
#         new_turtle.color(color)
#         new_turtle.penup()
#         new_turtle.goto(move)
#         turtles_list.append(new_turtle)
#
# snake_body(shape = "square", color = "white")

def create_snake():
    for move in snake_moves:
        add_segment(move)
def add_segment(position):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position)
    turtles_list.append(new_turtle)
def extend_snake():
    last_segment = turtles_list[-1]
    new_position = last_segment.position()
    add_segment(new_position)
create_snake()

