from turtle import *
tim = Turtle()
display = Screen()
number_of_times = 0
continuing = True
while continuing:
    number_of_times += 1
    for jog_space in range(0, 10):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()
        tim.forward(5)
    tim.left(90)
    for solid_line in range(10):
        tim.forward(5)
    if number_of_times == 50:
        continuing = False
        exit()
display.exitonclick()






