from requests import *
from twilio.rest import Client
ACCOUNT_SID = "ACaf558fa5a2e4b53d3e6c85ae8b6104a6"
AUTH_TAKEN = "25c517ee2dbf11a6fd15cbcbef1db5d3"

STOCK_NAME = "IBM"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_ENDPOINT_API = "39DHRV3MREKJZYLH"

ibm_stock_paramters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API
}
response = get(url = STOCK_ENDPOINT, params = ibm_stock_paramters).json()
# yesterday_closing_price = float(response["Time Series (Daily)"]["2024-12-09"]["4. close"])  # Not a useful approach; see; 2024-12-09 - - - - we are going to use List Comprehension

#step - 1: Getting IBM's yesterday stock price
stock_price = response["Time Series (Daily)"]
stock_price_list = [value for (key, value) in stock_price.items()]
yesterday_close_price = stock_price_list[0]["4. close"]
# print(yesterday_close_price)

#step - 2: Getting the day before yesterday's stock price of the company
the_day_before_yesterday = stock_price_list[1]["4. close"]
# print(the_day_before_yesterday)

#step - 3: positive difference between yesterday and the day before yesterday
difference = abs((float(yesterday_close_price) - float(the_day_before_yesterday)))
# print(difference)

#step - 4: work out the percentage difference between the two days' price
percentage_diff = (difference / float(yesterday_close_price)) * 100
# print(percentage_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 0:
    # print("Get News!")
    news_param = {
        "apikey": "3a2c34672cf1424b895e55861fee69d0",
        "qInTitle": "ibm"
    }
    response = get(url = "https://newsapi.org/v2/everything", params = news_param).json()["articles"]
    three_articles = response[:3]
    # print(three_articles)

    articles_description = [f"Headline: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]
    client = Client(ACCOUNT_SID, AUTH_TAKEN)
    for article in articles_description:

        message = client.messages.create(
            body = article,
            from_ = "whatsapp:+14155238886",
            to = "whatsapp:+15185330226"
        )








