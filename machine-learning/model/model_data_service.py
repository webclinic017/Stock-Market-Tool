#  d = {'col1': [1, 2], 'col2': [3, 4]}
# >>> df = pd.DataFrame(data=d)
import json

class ModelDataService:

    def get_ticker_df(ticker):
        print('hi')

request_url = 'http://localhost:3000/api/security/getReportedTicker'
request = { 'ticker': 'KMX' }
response = requests.get(url = request_url, data = request)
