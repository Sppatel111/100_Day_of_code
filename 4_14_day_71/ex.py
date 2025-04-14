import requests
import time

def get_stock_price(symbol, interval, api_key, exchange=None):
    if exchange:
        url = f"https://api.twelvedata.com/ad?symbol={symbol}&exchange={exchange}&interval={interval}&apikey={api_key}"
    else:
        url = f"https://api.twelvedata.com/ad?symbol={symbol}&interval={interval}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()
    print("data:")
    print(data)

    try:
    
        if 'values' in data and len(data['values']) > 0:
            current_price = float(data['values'][0]['ad'])
            return current_price
        else:
            print(f"Error fetching data for {symbol}: {data.get('message', 'No data available')}")
            return None
    except KeyError:
        print(f"Error fetching data for {symbol}: {data.get('message', 'Unknown error')}")
        return None


def track_stocks(symbols, interval, api_key, exchange=None):
    previous_prices = {symbol: None for symbol in symbols}
    print(previous_prices)

    while True:
        for symbol in symbols:
            current_price = get_stock_price(symbol, interval, api_key, exchange)
            if current_price is not None:
                if previous_prices[symbol] is not None:
                    if current_price > previous_prices[symbol]:
                        print(f"{symbol}: ${current_price:.2f} ↑")
                    elif current_price < previous_prices[symbol]:
                        print(f"{symbol}: ${current_price:.2f} ↓")
                    else:
                        print(f"{symbol}: ${current_price:.2f} →")
                else:
                    print(f"{symbol}: ${current_price:.2f} (initial price)")

                previous_prices[symbol] = current_price

        time.sleep(60)


if __name__ == "__main__":
    symbols = input("Enter stock symbols separated by commas (e.g., AAPL, INFY): ").split(',')
    interval = input("Enter the interval (e.g., 1min, 1day): ")
    exchange = input("Enter the exchange (leave blank if not applicable): ").strip() or None
    api_key = input("Enter your Twelve Data API key: ").strip()  # Get API key from user
    track_stocks([symbol.strip() for symbol in symbols], interval, api_key, exchange)
