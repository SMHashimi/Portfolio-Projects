from tkinter import *
from requests import *

kanye_window  = Tk()
kanye_window.title("Kanye Says...")

def get_quote():
    kanye_endpoints = get(url="https://api.kanye.rest/")
    kanye_quotes_dict = kanye_endpoints.json()
    kanye_quotes = kanye_quotes_dict["quote"]
    kanye_canvas.itemconfig(quotation, text = kanye_quotes, font = ("Courier", 15, "italic", "bold"), fill = "black")


kanye_canvas = Canvas(width = 300, height = 414)
background_img = PhotoImage(file = "background.png")
kanye_canvas.create_image(150, 207, image = background_img)
quotation = kanye_canvas.create_text(150, 207, text = "Kanye Quote Goes Here", width = 250, font = ("Ariel", 30, "bold"), fill = "white")
kanye_canvas.grid(column = 0, row = 0)

kanye_photo = PhotoImage(file = "kanye.png")
kanye_button = Button(image = kanye_photo, highlightthickness = 0, command = get_quote)
kanye_button.grid(column = 1, row = 1)








kanye_window.mainloop()
