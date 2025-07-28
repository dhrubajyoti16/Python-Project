import pandas as pd
from datetime import datetime

# Function to get stock data
def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=compact'
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.apply(pd.to_numeric)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return df

# Function to calculate moving average
def calculate_moving_average(df, window=5):
    df['Moving Average'] = df['4. close'].rolling(window=window).mean()
    return df

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'YOUR_API_KEY'
symbol = 'AAPL'

# Get stock data
stock_data = get_stock_data(symbol, api_key)

# Calculate the 5-day moving average
stock_data = calculate_moving_average(stock_data)

# Display the latest moving average
latest_date = stock_data.index[-1]
latest_moving_average = stock_data['Moving Average'][-1]
latest_close_price = stock_data['4. close'][-1]

print(f'On {latest_date.date()}, the 5-day moving average for {symbol} is {latest_moving_average:.2f} and the closing price is {latest_close_price:.2f}.')