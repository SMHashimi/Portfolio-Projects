from tkinter import *

the_flash_window = Tk()
the_flash_window.title("The Flash Card Game")
the_flash_window.config(padx = 50, pady = 50, background = "#B1DDC6")

the_flash_canvas = Canvas(width = 800, height = 526, background = "#B1DDC6", highlightthickness = 0)
front_image = PhotoImage(file = "./images/card_front.png")
the_flash_canvas.create_image(400, 263, image = front_image)
the_flash_canvas.grid(column = 0, row = 0, columnspan = 2)

#Creating Texts (Title & Word)
the_flash_canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
the_flash_canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

#Creating the two buttons (right & wrong)
right_button_image = PhotoImage(file = "./images/right.png")
right_button = Button(image = right_button_image, highlightthickness = 0, bd = 0)
right_button.grid(column = 1, row = 2)

wrong_button_image = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(image = wrong_button_image, highlightthickness = 0, bd = 0)
wrong_button.grid(column = 0, row = 2)




the_flash_window.mainloop()