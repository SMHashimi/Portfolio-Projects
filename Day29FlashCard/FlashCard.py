from tkinter import *
import pandas
import random

def generate_french_word():
    words = pandas.read_csv("french_words.csv")
    en_fr_pairs = words.to_dict(orient='records')
    random_french_word = random.choice(en_fr_pairs)
    add_to_rightWrong_button = random_french_word["French"]
    french_to_english_meaning = [random_french_word[translation] for translation in random_french_word]
    # print(add_to_rightWrong_button)     #The French Word
    # print(french_to_english_meaning)    #The Meaning
    # print(french_to_english_meaning[1]) #Extracting the meaning
    the_flash_canvas.itemconfig(french_word, text = add_to_rightWrong_button)
    the_flash_canvas.itemconfig(french_title, text = "French", font = ("Ariel", 40, "italic"))

the_flash_window = Tk()
the_flash_window.title("The Flash Card Game")
the_flash_window.config(padx = 50, pady = 50, background = "#B1DDC6")

the_flash_canvas = Canvas(width = 800, height = 526, background = "#B1DDC6", highlightthickness = 0)
front_image = PhotoImage(file = "./images/card_front.png")
the_flash_canvas.create_image(400, 263, image = front_image)
the_flash_canvas.grid(column = 0, row = 0, columnspan = 2)

#Creating Texts (Title & Word)
french_title = the_flash_canvas.create_text(400, 150, font = ("Ariel", 40, "italic"))
french_word = the_flash_canvas.create_text(400, 263, font = ("Ariel", 60, "bold"))

#Creating the two buttons (right & wrong)
right_button_image = PhotoImage(file = "./images/right.png")
right_button = Button(image = right_button_image, highlightthickness = 0, bd = 0, command = generate_french_word)
right_button.grid(column = 1, row = 2)

wrong_button_image = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(image = wrong_button_image, highlightthickness = 0, bd = 0, command = generate_french_word)
wrong_button.grid(column = 0, row = 2)

generate_french_word()
the_flash_window.mainloop()