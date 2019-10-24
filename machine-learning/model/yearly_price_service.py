import json

class YearlyPriceService:
    def get_avg_price(self, ticker, year, filepath):
        price_data = self.get_price_data_json(ticker, year, filepath)
        return self.compute_avg_price(price_data, year) 

    def get_price_data_json(self, ticker, year, filepath):
        json_file = filepath + f'{ticker}-price-daily.json'
        with open(json_file) as f:
            response = json.load(f)
            price_data = response['Time Series (Daily)']
        return price_data
        

    def compute_avg_price(self, price_data, year):
        number_of_dates = 0
        total_price_of_dates = 0
        for date in price_data:
            if year in date:
                total_price_of_dates += float(price_data[date]['5. adjusted close'])
                number_of_dates += 1
        
        if number_of_dates != 0:
            avg_price = total_price_of_dates / number_of_dates
            return avg_price
        return 0
