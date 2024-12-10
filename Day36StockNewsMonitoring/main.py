from requests import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_ENDPOINT_API = "39DHRV3MREKJZYLH"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

ibm_stock_paramters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": STOCK_ENDPOINT_API
}
response = get(url = STOCK_ENDPOINT, params = ibm_stock_paramters).json()
# yesterday_closing_price = float(response["Time Series (Daily)"]["2024-12-09"]["4. close"])  # Not a useful approach; see; 2024-12-09 - - - - we are going to use List Comprehension

#step - 1: Getting IBM's yesterday stock price
yesterday_closing_price = response["Time Series (Daily)"]
yesterday_closing_price_list = [value for (key, value) in yesterday_closing_price.items()]
print(yesterday_closing_price_list[0])

#step - 2: Getting the day before yesterday's stock price of the company
the_day_before_yesterday = yesterday_closing_price_list[1]
print(the_day_before_yesterday)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#step - 3: getting the positive difference between step 1 and 2
yesterday_close_price = "350"
the_day_before_yesterday_price = "400"
print(abs(int(yesterday_close_price) - int(the_day_before_yesterday_price)))











#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

