from smtplib import *
MY_EMAIL = "mubaris.hashimi2018@gmail.com"
PASSWORD = "unqyvpdpwymjkpvq"

connection = SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = MY_EMAIL, password = PASSWORD)
connection.sendmail(from_addr = MY_EMAIL, to_addrs = "mubaris.hashimi@auaf.edu.af", msg = "Subject: Python Automation\n\nDear Hashimi,\n\nI hope"
                                                                            " this email finds you well and healthy."
                                                                            " I wanted to inform you that due to some"
                                                                            " some reasons, I cannot join tomorrow's meeting."
                                                                            " I hope you understand my situations. Furthermore, this email is sent through Python"
                                                                            " through Python automation facility, and not the Gmail itself."
                                                                            "\n\nRegards,\nSayed Mubaris Hashimi - Me")
connection.close()