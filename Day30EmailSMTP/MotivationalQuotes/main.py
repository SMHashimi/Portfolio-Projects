from datetime import *
from smtplib import *
import random

MY_EMAIL = "mubaris.hashimi2018@gmail.com"
PASSWORD = "ojsz sfaq nsib avbd"

curent_date = datetime.now()
print(curent_date)
week_day  = curent_date.weekday()

#In python, the first day of the week (which is Monday) is 0; so, today is Saturday for me.
#monday = 0
#tuesday = 1
#wednesday = 2
#thursday = 3
#friday = 4
#saturday = 5
#sunday = 6

if week_day == 5:
    with open ("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        random_number =  random.randint(0, len(all_quotes) - 1)
        print(all_quotes[random_number])
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = "mubaris.hashimi@auaf.edu.af",
            msg = f"Subject: Saturday Motivation\n\nDear Hashimi,\n\n{all_quotes[random_number]}\nRegards,")
        connection.close()


