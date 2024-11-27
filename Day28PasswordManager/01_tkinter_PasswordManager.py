from tkinter import *
from tkinter import messagebox   #it is not a class to import
import random
from LettersNumbersSymbols import *
import pyperclip
import json

the_manager_window = Tk()
the_manager_window.title("Password Manager")
the_manager_window.config(padx = 50, pady = 50)

the_manager_canvas = Canvas(width = 200, height = 200)
logo_image = PhotoImage(file = "logo.png")
the_manager_canvas.create_image(100, 100, image = logo_image)
the_manager_canvas.grid(column = 1, row = 0)

def make_password():
    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    random_chosen_password = ""
    random_chosen_password_list = []
    for letter in range(0, nr_letters):
        random_chosen_letters = random.choice(letters)
        random_chosen_password += random_chosen_letters
    for symbol in range(0, nr_symbols):
        random_chosen_symbols = random.choice(symbols)
        random_chosen_password += random_chosen_symbols
    for number in range(0, nr_numbers):
        random_chosen_numbers = random.choice(numbers)
        random_chosen_password += random_chosen_numbers
    random_chosen_password_list += random_chosen_password
    # print(random_chosen_password_list)
    random.shuffle(random_chosen_password_list)
    # print(random_chosen_password_list)
    final_password = ""
    for key in random_chosen_password_list:
        final_password += key
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)

def save():
    website = website_entry.get().title()
    try:
        with open("./user_data.json", mode="r") as data:  # updating data - adding (NOT appending) a new data
            if len(website) == 0 or len(password_entry.get()) == 0:
                messagebox.showwarning(title="Error", message="Please do not leave any spot empty!")
            elif len(website) != 0 and len(password_entry.get()) != 0:
                user_info = {
                    website: {
                        "E-mail": email_entry.get(),
                        "Password": password_entry.get()
                    }
                }
                user_data = json.load(data)  # Step 1 - Loading the existing data
                user_data.update(user_info)  # Step 2 - Updating in the existing data
                with open("user_data.json", mode="w") as data:
                    json.dump(user_data, data, indent=4)  # Step 3 - Dumping the updates
                f"{website_entry.delete(0, END)} {password_entry.delete(0, END)}"
    except FileNotFoundError:
        with open("user_data.json", mode = "w") as data:
            user_info = {
                website: {
                    "E-mail": email_entry.get(),
                    "Password": password_entry.get()
                }
            }
            json.dump(user_info, data, indent = 4)
            f"{website_entry.delete(0, END)} {password_entry.delete(0, END)}"

def search():
    try:
        with open("./user_data.json", mode = "r") as search_data:
            data_dict = json.load(search_data)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error",
                            message = "No Data Found")
    else:
        if website_entry.get().title() not in data_dict or len(website_entry.get().title()) == 0:
            messagebox.showinfo(title="Error",
                                message="Non-existent Item or Empty Field")
        for key, value in data_dict.items():
            if (website_entry.get().title()) == key:
                messagebox.showinfo(title = f"{key}",
                                    message = f"Email: {value["E-mail"]}\n"
                                              f"Password: {value["Password"]}" )

#making website label and entry
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
website_entry = Entry(width = 21)
website_entry.focus()
website_entry.grid(column = 1, row = 1)

#making email label and entry
email_Username = Label(text = "Email/Username:")
email_Username.grid(column = 0, row = 2)
email_entry = Entry(width = 52)
email_entry.insert(0, "Mubaris.hashimi2018@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan = 2, pady = 1)

#making password label and entry
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)
password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

#making generate password button
generate_password = Button(text = "Generate Password", command = make_password)
generate_password.grid(column = 2, row = 3, pady = 2)

#making add button
add_button = Button(text = "Add", width = 44, command = save)
add_button.grid(column = 1, row = 4, pady = 5, columnspan = 2)

#making search button
search_button = Button(text = "Search", width = 14, command = search)
search_button.grid(column = 2, row = 1, pady = 2)

the_manager_window.mainloop()
