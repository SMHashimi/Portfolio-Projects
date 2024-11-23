import math
from tkinter import *

#https://colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
count_down_time = None

def the_Pomodoro_technique():

    def reset():
        the_app_window.after_cancel(count_down_time)
        the_app_canvas.itemconfig(count_down_timer, text = "00:00")
        timer_label.config(text = "Timer")
        checkmark.config(text = "")
        global rep
        rep = 0

    def count_down(count):
        count_min = math.floor(count / 60)
        count_sec  = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        the_app_canvas.itemconfig(count_down_timer, text = f"{count_min}:{count_sec}")
        if count > 0:
            global count_down_time
            # print(count)
            count_down_time = the_app_window.after(1000, count_down, count -1 )  #Make it global for cancellation
        else:
            timer_down()
            ticks = ""
            every_two_completion = math.floor(rep / 2)
            for _ in range(every_two_completion):
                ticks += "✔"
            checkmark.config(text = ticks, font = (FONT_NAME, 10, "bold"), fg = GREEN, bg = "#913175", highlightthickness = 0)

    #Countin down from 5 when Start button is triggered
    def timer_down():
        global rep
        rep += 1
        if rep % 8 == 0:
            timer_label.config(text = "Long Break", font = (FONT_NAME, 30, "bold"), fg = RED, bg = "#913175", highlightthickness = 0)
            count_down(LONG_BREAK_MIN * 60)
        elif rep % 2 == 0:
            timer_label.config(text = "Short Break", font = (FONT_NAME, 30, "bold"), fg = PINK, bg = "#913175", highlightthickness = 0)
            count_down(SHORT_BREAK_MIN * 60)
        else:
            timer_label.config(text = "Work", font = (FONT_NAME, 30, "bold"), fg = GREEN, bg = "#913175", highlightthickness = 0)
            count_down(WORK_MIN * 60)

    the_app_window = Tk()
    the_app_window.title("The Pomodoro App")
    # the_app_window.config(padx = 100, pady = 50, bg = YELLOW)

    the_app_canvas = Canvas(width = 700, height = 680, bg = "#913175", highlightthickness = 0)
    the_app_image = PhotoImage(file = "tomato.png")
    the_app_canvas.create_image(350, 350, image = the_app_image)
    count_down_timer = the_app_canvas.create_text(350, 350, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))

    #TimerLabel
    timer_label = Label(text = "Timer", font = (FONT_NAME, 30, "bold"), fg = GREEN, bg = "#913175", highlightthickness = 0)
    timer_label.grid(column = 1, row = 0)

    #Start Button
    start_button = Button(text = "Start", font = (FONT_NAME, 10, "bold"), highlightthickness = 0, command = timer_down)
    start_button.grid(column = 0, row = 1)

    ##Reset Button
    reset_button = Button(text = "Reset", font = (FONT_NAME, 10, "bold"), highlightthickness = 0, command = reset)
    reset_button.grid(column = 2, row = 1)

    #checkmark
    #https://en.wikipedia.org/wiki/Check_mark
    checkmark = Label(fg = GREEN, bg = "#913175")
    checkmark.grid(column = 1, row = 1)

    the_app_canvas.grid(column = 0, row = 0, columnspan = 3, rowspan = 2)
    the_app_window.mainloop()


