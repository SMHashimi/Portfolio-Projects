
import random
import game_data
import art

def random_chosen_figure_A(a):
    return f'Compare A: {a["name"]}, A {a["description"]} from {a["country"]}'

def random_chosen_figure_B(b):
    return f'Against B: {b["name"]}, A {b["description"]} from {b["country"]}'

def game_play():
    game = True
    your_score = 0
    # print(art.logo)
    # print(random_chosen_figure_A())
    # print(art.vs)
    # print(random_chosen_figure_B())
    while game:
        a = random.choice(game_data.data)
        print(random_chosen_figure_A(a))
        print(art.logo)

        b = random.choice(game_data.data)
        print(random_chosen_figure_B(b))
        print(art.vs)
        followers_a = a["follower_count"]
        followers_b = b["follower_count"]
        follower_amount = input("Who has more followers? Type A or B: ")
        if follower_amount == "A".lower():
            if followers_a > followers_b:
                your_score += 1
                print(f"You're right! Current score: {your_score}")
            else:
                return f"Sorry, that's wrong. Final Score: {your_score}"
                # game = False
        elif follower_amount == "B".lower():
            if followers_b > followers_a:
                your_score += 1
                print(f"You're right! Current score: {your_score}")
            else:
                # game = False
                return f"Sorry, that's wrong. Final Score: {your_score}"

play_game = game_play()
print(play_game)











