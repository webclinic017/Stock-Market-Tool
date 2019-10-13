# yearly_price_service.py must be in same directory as file doing import.
from yearly_price_service import YearlyPriceService

# Instantiate object.
yearly_price_service = YearlyPriceService()

# Call method.
#    I have wrapped this in a try, except block. I suggest you do the same.
#    Otherwise, if you give it a ticker it does not expect, it will return a FileNotFoundError

# The first parameter is a string of the ticker.
# The second parameter is a string of the desired year.
# The third parameter is a string of the file path from the file you are writing to the json-data folder.
#    (NOTE): the trailing '/' is required.
try:
    print(yearly_price_service.get_avg_price('GOOG', '2005', '../machine-learning/data/alpha-vantage/json-data/'))
except:
    print('Ticker not found!')

# The return type is a float of the average adjusted closing price for that year.
# If you have requested a year for which no data is available (such as 'GOOG', '2000'), it will return 0.
