from idlelib.colorizer import prog_group_name_to_tag

from turtle_01_USStatesGuessGame import *
import pandas

US_states_data = pandas.read_csv("50_states.csv")
# print(US_states_data)

USStatesToList = US_states_data.state.to_list()
# print(USStatesToList)


user_guessed_list = []
def pointing_states_location():
    if user_StatesInquiry in USStatesToList:
        indicator = Turtle()
        indicator.penup()
        indicator.hideturtle()
        user_chosen_state = US_states_data[US_states_data.state == user_StatesInquiry]
        # print(user_chosen_state)
        indicator.goto(user_chosen_state.x.item(), user_chosen_state.y.item())
        indicator.write(user_StatesInquiry)

while len(user_guessed_list) < 50:
    user_StatesInquiry = screen.textinput(f"{len(user_guessed_list)} of 50", "Please guess a state:").title()
    if user_StatesInquiry == "Exit":
        missed_guessed_states = [state for state in USStatesToList if state not in user_guessed_list]
        print(missed_guessed_states)
        missed_states = pandas.DataFrame(missed_guessed_states)
        missed_states.to_csv("to_learn_in_the_future.csv")
        break

    user_guessed_list.append(user_StatesInquiry)
    # print(user_guessed_list)
    pointing_states_location()

# screen.mainloop()





























# print(user_chosen_state)
# x = user_chosen_state["x"].to_list()
# y = user_chosen_state["y"].to_list()
# print(user_chosen_state.x)

