from turtle_SnakeTailCollision import *

import random
import time
moving_snake = True
while moving_snake:
    screen.update()
    time.sleep(0.1)

    # for turtle in turtles_list:
    #     turtle.forward(20)

    for turtle_num in range(len(turtles_list) - 1, 0, -1):
        x_cordinate = turtles_list[turtle_num - 1].xcor()
        y_cordinate = turtles_list[turtle_num - 1].ycor()
        turtles_list[turtle_num].goto(x_cordinate, y_cordinate)
    turtles_list[0].forward(20)

    if turtles_list[0].xcor() > 350 or turtles_list[0].xcor() < -350 or turtles_list[0].ycor() > 350 or turtles_list[0].ycor() < -350:
        collision_wall()

    if turtles_list[0].distance(tim) < 15:
        if turtles_list[0].distance(tim) < 15:
            extend_snake()
            score_board.clear()
            score += 1
            score_board.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
            print(score)

            random_location_x = random.randint(-320, 320)
            random_location_y = random.randint(-320, 320)
            tim.goto(random_location_x, random_location_y)

    ##Collision with tail -
    for segment in turtles_list[1:]:
        if turtles_list[0].distance(segment) < 10:
            moving_snake = False
            score_board.goto(0, 0)
            score_board.write("GAME OVER", align  = "center", font = "Courier")

screen.exitonclick()










