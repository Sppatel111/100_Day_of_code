import time
import requests


# curl --request GET
# 	--url 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary?region=US&symbol=AMRN'
# 	--header 'x-rapidapi-host: apidojo-yahoo-finance-v1.p.rapidapi.com'
# 	--header 'x-rapidapi-key: d6d12e748amshff2bb4fa69cea8fp15c5d0jsn90b3bbcb5a91'

def get_stock_price(symbol):
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary'

    querystring = {"region": "US", "symbol":symbol}

    headers = {
        "x-rapidapi-key": "d6d12e748amshff2bb4fa69cea8fp15c5d0jsn90b3bbcb5a91",
        "x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response)
    data = response.json()
    print(data)

    try:
        current_price = data['price']['regularMarketOpen']['raw']
        print(current_price)
        return current_price
    except Exception as e:
        print(f"error fetching data for {symbol}:{data.get('message', 'unknown error')}")
        return None


get_stock_price('AMRN')


def track_stocks(symbols, intervals):
    pass
