from tkinter import *

#Importing Tk class (from tkinter module) - and setting up the window size
widget_window = Tk()
widget_window.title("Mile to Km Converter")
widget_window.minsize(height = 145, width = 500)

#The app introduction
widget_label = Label(text = "Welcome to the Kilometer Converter",
                     font = ("Arial", 15, "bold", "italic"))
widget_label.grid(column = 1, row = 0, pady = 10)

#UserInput - Putting their number to convert
user_input = Entry(width = 10)
user_input.insert(END,0)
user_input.focus()
user_input.grid(column = 1, row = 1)

#Creating Miles label
length_unit = Label(text = "Miles",
                    font = ("Arial", 10))
length_unit.grid(column = 2, row = 1)

#Creating 'is equal to' lable
equality = Label(text = "is equal to",
                 font = ("Arial", 10))
equality.grid(column = 0, row = 2)

#Making an entry for the result
the_result = Label(text = "0", width = 10)
# the_result.insert(END, 0)
the_result.grid(column = 1, row = 2)

#Creating Km label
length_unit = Label(text = "Km",
                    font = ("Arial", 10))
length_unit.grid(column = 2, row = 2)

#defining the function
def calculate():
    # print("I got clicked!")
    mile = float(user_input.get())
    result = round((mile * 1.61), 3)
    # print(result)
    the_result.config(text = f"{result}")

#Calculating the input
calculate = Button(text = "Calculate",
                   font = ("Arial", 10, "bold"), command = calculate)
calculate.grid(column = 1, row = 3, pady = 10)

widget_window.mainloop()
