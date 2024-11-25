from tkinter import *

themanager_window = Tk()
themanager_window.title("Password Manager")
themanager_window.config(padx = 20, pady = 20)

themanager_canvas = Canvas(width = 200, height = 200)
themanager_image = PhotoImage(file = "logo.png")
themanager_canvas.create_image(100, 100, image = themanager_image)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#



themanager_canvas.grid()
themanager_window.mainloop()