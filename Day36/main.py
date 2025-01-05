import requests #type: ignore
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()  

STOCK_API_KEY = os.getenv("STOCK_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "TSLA"

NEWS_API_KEY = os.getenv("NEWS_KEY")
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT,stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]


data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(difference)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)



if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
    three_articles = articles[:3]


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        print(article)
    





