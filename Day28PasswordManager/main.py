from tkinter import *

the_manager_window = Tk()
the_manager_window.title("Password Manager")
the_manager_window.config(padx = 50, pady = 50)

the_manager_canvas = Canvas(width = 200, height = 200)
logo_image = PhotoImage(file = "logo.png")
the_manager_canvas.create_image(100, 100, image = logo_image)
the_manager_canvas.grid(column = 1, row = 0)

#making website label and entry
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
website_entry = Entry(width = 52)
website_entry.grid(column = 1, row = 1, columnspan = 2)

#making email label and entry
email_Username = Label(text = "Email/Username:")
email_Username.grid(column = 0, row = 2)
email_entry = Entry(width = 52)
email_entry.grid(column = 1, row = 2, columnspan = 2)

#making password label and entry
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)
password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

# making generate password button
generate_password = Button(text = "Generate Password")
generate_password.grid(column = 2, row = 3)

# making add button
add_button = Button(text = "Add", width = 44)
add_button.grid(column = 1, row = 4, columnspan = 2, pady = 5)

the_manager_window.mainloop()