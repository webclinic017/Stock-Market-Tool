import json
import requests
import pandas as pd
from yearly_price_service import YearlyPriceService

class ModelDataService:
    request_url = 'http://localhost:3000/api/security/getReportedTicker'
    # 97-2013
    Y = [7.23, 6.48, 7.03, 7.65, 7.10, 6.42, 5.68, 5.63, 5.25, 5.51, 5.53, 5.40, 5.25, 4.94, 4.51, 3.70, 4.24]

    # return x1, x2, and y
    # this is detailed in notes.md 
    def get_ticker_df(self, ticker):
        # 97-13 (17)  Jan, May, Sept, Dec
        Y = self.Y

        x1_list = []
        x2_list = []
        y_list = []
        year_list = []
        yearly_price_service = YearlyPriceService()
        resJson = self.get_ticker_data(ticker)
        
        j = 16
        i = 0
        while i < len(resJson['fiscalYears']):
            # Calculate EPS.
            try:
                dilWeightAvgShares = resJson['fiscalYears'][i]['incomeSheet']['dilWeightAvgShares']
                niAvailCommonGaap = resJson['fiscalYears'][i]['incomeSheet']['niAvailCommonGaap']
                EPS = niAvailCommonGaap / dilWeightAvgShares
            except:
                i += 1
                continue

            # Calculate growth rate.
            grow_rate = 1
            if i != 0:                
                try:
                    priorDilWeightAvgShares = resJson['fiscalYears'][i-1]['incomeSheet']['dilWeightAvgShares']
                    priorNiAvailCommonGaap = resJson['fiscalYears'][i-1]['incomeSheet']['niAvailCommonGaap']
                    priorEPS = priorNiAvailCommonGaap / priorDilWeightAvgShares
                    grow_rate = (EPS - priorEPS)/priorEPS
                except:
                    i += 1
                    continue

            # Get avg price in 5 years.
            try:
                current_year_plus_5 = str(int(resJson['fiscalYears'][i]['year']) + 5)
                if int(current_year_plus_5) > 2018:
                    i += 1
                    continue 

                y = yearly_price_service.get_avg_price(f'{ticker}', f'{current_year_plus_5}', '../data/alpha-vantage/json-data/')
                if y == 0:
                    i +=1
                    continue
            except:
                i += 1
                continue

            x1 = ((4.4 * EPS) / Y[j])
            j -= 1
            x1_list.append(x1)
            
            x2 = x1 * grow_rate
            x2_list.append(x2)

            y_list.append(y)
            
            year_list.append(int(current_year_plus_5) - 5)

            # Advance year.
            i += 1

        print(pd.DataFrame({'year': year_list, 'x1': x1_list, 'x2': x2_list, 'y': y_list}))
        return pd.DataFrame({'x1': x1_list, 'x2': x2_list, 'y': y_list})

    def get_ticker_data(self, ticker):
        request = { 'ticker': f'{ticker}' }
        response = requests.post(url = self.request_url, data = request)
        return response.json()


model_data_service = ModelDataService()
model_data_service.get_ticker_df('HRB')
