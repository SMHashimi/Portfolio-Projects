from idlelib.run import MyHandler

from bs4 import BeautifulSoup
from requests import *
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

instant_pot = "https://appbrewery.github.io/instant_pot/"
response = get(url = instant_pot)

soup = BeautifulSoup(response.text, "html.parser")
the_product_price_without_currency = soup.find(name = "span", class_ = "a-offscreen").getText().split("$")[1]

if float(the_product_price_without_currency) <= 100:
    from smtplib import *
    buying_link = ("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_"
                   "1_1?dib=eyJ2IjoiMSJ9.5s_5RS4qKJMOxc04dnxdoss-"
                   "L7XfL35kgkFImE1NyQNcAF5EVwDcxau8hFO1CVmZIVE57dn92fpxJ2JdGtXOKeiYFLdndW8_"
                   "gjDRxvIPYJ47Ju1OHkURzzCut58E37kXyrYDGEGQMbdF5ciX9TR1yScaxtPVJBjUmQZc_aVwk97HOU7QJ"
                   "-txcs1Npn-qRpN-kbKuhfRcdiBtGUJ3H53bLbJJhE8jqxRYqHn6X3AENdw."
                   "-JJggdopyEOWZpDuez49hhvxvp72oZPJiFLBBOeVyCE&dib_tag=se&hvadid="
                   "377801081472&hvdev=c&hvlocphy=1022672&hvnetw"
                   "=g&hvqmt=e&hvrand=3514574006365180838&hvtargid=kwd-308526824823&hydadcr="
                   "1776_9636512&keywords=instant%2Bpot%2Bamazon&qid=1734491213&sr=8-1&th=1")

    MY_EMAIL = os.getenv("MY_EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    connection = SMTP(os.getenv("SMTP_ADDRESS"))
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs = MY_EMAIL,
                        msg="Subject: Instant Pot\n\nDear Hashimi,\n\nI hope"
                            " this email finds you well and healthy."
                            " I wanted to inform you that the price for the product"
                            " Instant Pot has fallen below 100. The price and the link to buy it"
                            " is provided below:\nThe price is: $" + the_product_price_without_currency +
                            "\nThe link:\n" + buying_link + "\n\nRegards,\nSayed Hashimi")
    connection.close()

