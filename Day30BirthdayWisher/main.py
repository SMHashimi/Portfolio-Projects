from smtplib import *
import random
import pandas
from datetime import *

current_date = datetime.now()
# print(current_date)
# print(current_date.year)
# print(current_date.month)
# print(current_date.day)


birthday_data = pandas.read_csv("birthdays.csv")
people_list = birthday_data.to_dict(orient = "records")
random_choses_person = random.choice(people_list)
# print(random_choses_person)

MY_EMAIL = "mubaris.hashimi2018@gmail.com"
PASSWORD = "oqok zuba gsny bjgh"

random_name = random_choses_person["name"]
# print(random_name)

name_holder = "[NAME]"
with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", mode = "r") as letters:
    # file = letters.read()
    file = letters.readlines()
for item in file:
    trimmed_item = item.strip()
    # print(trimmed_item)
with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", mode = "r") as completed_letters:
    letter = completed_letters.read()
    # print(letter)
# if name_holder in letter:
#     replacement = letter.replace(name_holder, random_name)

for index, row in birthday_data.iterrows():

    if name_holder in letter:
        replacement = letter.replace(name_holder, row["name"])
    # print(row["name"])
    if (current_date.month) == row["month"] and (current_date.day) == row["day"]:
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL, to_addrs = row["email"], msg = f"Subject: Birthday Wisher\n\n{replacement}\nRegards,")
        # print(replacement)
        connection.close()




























