import yearly_price_service
import glob
import Calcs

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

def getPrices(symbol, years):
	path = './'
	prices = []
	#Creates JSON objects for database:
	i = 1
	years = iter(years)
	next(years)
	for year in years:
		try:
			price = yearly_price_service.get_avg_price(symbol, year, '../machine-learning/data/alpha-vantage/json-data/')
			if(price != 0):
				prices.append(round(price, 3))
			else:
				prices.append(-1)
		except:
			prices.append(-1)
		i += 1

	return prices
# The return type is a float of the average adjusted closing price for that year.
# If you have requested a year for which no data is available (such as 'GOOG', '2000'), it will return 0.