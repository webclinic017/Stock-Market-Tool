import numpy as np
import pandas as pd 
import glob
import os
import json
import re

#Read initial xlsx files:
#tickers = glob.glob("*.xlsx")
ticker = "GOOGL.xlsx"
i = 0
j=0
#for ticker in tickers:

inc = pd.DataFrame(pd.read_excel(ticker, sheet_name='Income - GAAP'))
bal = pd.DataFrame(pd.read_excel(ticker, sheet_name='Bal Sheet - Standardized'))
cf = pd.DataFrame(pd.read_excel(ticker, sheet_name='Cash Flow - Standardized'))

rows_inc, cols_inc = inc.shape
rows_bal, cols_bal = bal.shape
rows_cf, cols_cf = cf.shape

inc = inc.drop(inc.columns[[1]],axis=1)
bal = bal.drop(bal.columns[[1]],axis=1)
cf = cf.drop(cf.columns[[1]],axis=1)

inc = inc.reset_index(drop=True)
bal = bal.reset_index(drop=True)
cf = cf.reset_index(drop=True)

inc.dropna(axis=0, how='all', inplace=True)

for index, row in inc.iterrows():
    print(index, str(row[0]).strip())

j= j+1
if(rows_inc < 50 ):
    i = i + 1

print(str(j) + ": number of tickers below 50 lines " + str(i) )
