from turtle_5_PlayerAtOriginANDCollision import *
import time

while game_is_on:
    time.sleep(0.16)
    screen.update()
    car_creation()
    back_at_origin()

    for car in cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            game_over()

screen.exitonclick()