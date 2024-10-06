from turtle import *
import random
screen = Screen()
screen.setup(700, 600)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
print(user_bet)
racing  = True
Turtles = []
colors = ["gold1", "chartreuse2", "DarkOliveGreen", "DeepPink1", "cyan", "CornflowerBlue"]  #https://cs111.wellesley.edu/labs/lab02/colors
vertical_position = [-100, -60, -20, 20, 60, 100]
speed = [2, 1.8, 1.59, 3.2, 1.1, 4.1, 1.5]
for turtle_position in range(6):
    all_turtles = Turtle(shape ="turtle")
    all_turtles.penup()
    all_turtles.color(colors[turtle_position])
    all_turtles.goto(x = -340, y = vertical_position[turtle_position])
    Turtles.append(all_turtles)
while racing:
    for turtle in Turtles:
        if turtle.xcor() > 340:   ##+340 is the opposite (to the right side of x-coordinate)
            racing = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won. The winner is {winner}")
            else:
                print(f"Your bet turned to be wrong. The winner is {winner}.")
        turtle.forward(random.choice(speed))
screen.exitonclick()
