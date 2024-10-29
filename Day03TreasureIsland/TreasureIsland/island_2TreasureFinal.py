from island_1TreasureASCIIART import treasure_island
print(treasure_island)


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

ask_direction = input("Please choose your direction: right or left?  ").lower()
if ask_direction == "right":
    print("You fell into a hole\nGame Over.")

elif ask_direction == "left":
    swim_or_wait = input("Do you wanna 'swim' or 'wait'? ").lower()
    if swim_or_wait == "swim":
        print("You have been attacked by trout\nGame Over.")
    elif swim_or_wait == "wait":
        which_door = input("Through which door, you wanna proceed? 'Blue' 'Red' 'Yellow': ").lower()
        if which_door == "blue":
            print("You have been eaten by beasts\nGame Over.")
        elif which_door == "red":
            print("You are burned by fire.\nGame Over.")
        elif which_door == "yellow":
            print("Congratualtions, you win!")
        else:
            print("Game Over.")
    else:
        print("You have been attacked by trout.\nGame Over.")
else:
    print("You fell into a hole\nGame Over.")




