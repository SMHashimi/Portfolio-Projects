from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

the_app_window = Tk()
the_app_window.title("The Pomodoro App")
# the_app_window.config(padx = 100, pady = 50, bg = YELLOW)

the_app_canvas = Canvas(width = 700, height = 680, bg = YELLOW, highlightthickness = 0)
the_app_image = PhotoImage(file = "tomato.png")
the_app_canvas.create_image(350, 350, image = the_app_image)
the_app_canvas.create_text(350, 350, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))

#TimerLabel
timer_label = Label(text = "Timer", font = (FONT_NAME, 30, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
timer_label.grid(column = 1, row = 0)

#Start Button
start_button = Button(text = "Start", font = (FONT_NAME, 10, "bold"), highlightthickness = 0)
start_button.grid(column = 0, row = 1)

##Reset Button
reset_button = Button(text = "Reset", font = (FONT_NAME, 10, "bold"), highlightthickness = 0)
reset_button.grid(column = 2, row = 1)

#checkmark
checkmark = Label(text = "✔", font = (FONT_NAME, 10, "bold"), fg = GREEN, bg = YELLOW, highlightthickness = 0)
checkmark.grid(column = 1, row = 1)

the_app_canvas.grid(column = 0, row = 0, columnspan = 3, rowspan = 2)
the_app_window.mainloop()