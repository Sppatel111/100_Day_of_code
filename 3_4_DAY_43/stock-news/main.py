import requests
from twilio.rest import Client
from secret1 import TO,FROM,ACCOUNT_SID,AUTH_TOKEN,STOCK_API_KEY,NEWS_API_KEY

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_api_key =STOCK_API_KEY

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key=NEWS_API_KEY

#twilio
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN



#Use https://www.alphavantage.co/documentation/#daily
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}

r = requests.get(STOCK_ENDPOINT, params=stock_params)

data = r.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]

#yesterday closing price
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
# print(yesterday_closing_price)

#day before closing price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

#Find the positive difference
difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
# print(difference)
UP_DOWN= None
if difference >0:
    UP_DOWN ="🔺"
else:
    UP_DOWN="🔻"

#percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage=round((difference/float(yesterday_closing_price))*100)
# print(diff_percentage)

#news
#print(data1)
if abs(diff_percentage) >2:
    parameters = {
        'apiKey': news_api_key,
        'qInTitle':COMPANY_NAME
    }
    r1 = requests.get(NEWS_ENDPOINT, params=parameters)
    articles= r1.json()["articles"]

    three_articles=articles[:3]

    # \nBrief:{article['description'] not available
    formatted_article=[f"{STOCK_NAME}:{UP_DOWN}{diff_percentage}% \nheadline:{article['title']}" for article in three_articles]
    # print(formatted_article)

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body= article,
            from_=FROM,
            to=TO
        )
        print(message.status)


