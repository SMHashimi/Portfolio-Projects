
from RockPaperScissorsAsciiArt import *
import random

images =  [rock, paper, scissors]

user_choice = int(input("Please choose your option? 0 for Rock, 1 for Paper or 2 for scissors: "))
print(images[user_choice])

computer_choice = random.randint(0, 2)
print(f"The machine (computer) has chosen: {images[computer_choice]}")

if user_choice >= 3 and computer_choice < 0:
    print("Invalid Entry")
elif computer_choice == 0 and user_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win !")
elif computer_choice == user_choice:
    print("Draw")












