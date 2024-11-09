from turtle_3_CarsMoving import *
import time
game_is_on = True

while game_is_on:
    time.sleep(0.02)
    screen.update()
    car_creation()

screen.exitonclick()