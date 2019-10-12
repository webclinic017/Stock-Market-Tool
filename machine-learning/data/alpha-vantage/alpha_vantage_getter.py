import requests
import time
import json

# Constants
key = 'P4Y44752S9IOSDIC'

# Read list of S&P 500 stocks.
def populate_ticker_array(tickers):
    with open('./s&p500-companies.txt') as fp:
        line = fp.readline()
        while line:
            tickers.append(line.split("\t")[0])
            line = fp.readline()

# Create json file for each ticker in list.
def alpha_vantage_getter(tickers):
    for ticker in tickers:
        try:
            # Call Alpha Vantage API.
            request_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey=P4Y44752S9IOSDIC'
            response = requests.get(request_url)
            response.raise_for_status()

            # Write to file.
            with open(f'json-data/{ticker}-price-daily.json', 'w') as f:
                json.dump(response.json(), f)

            # Need to wait as we can only complete 5 requests a minute.
            time.sleep(20)
        except:
            print(f'{ticker} data capture failed')
        else:
            print(f'{ticker} data captured successfully')

def main_function():
    # get list of tickers
    tickers = []
    populate_ticker_array(tickers)

    # create json files
    alpha_vantage_getter(tickers)

main_function()
