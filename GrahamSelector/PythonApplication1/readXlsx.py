import numpy as np
import pandas as pd 
import glob
import os
import json
import re


#print 'all' to screen
pd.set_option("max_rows",2000)

#Adjust directory information
strXlsx = ".xlsx"

#Read initial xlsx files:
tickers = glob.glob("*.xlsx")

for ticker in tickers:

    inc = pd.DataFrame(pd.read_excel(ticker, sheet_name='Income - GAAP'))
    bal = pd.DataFrame(pd.read_excel(ticker, sheet_name='Bal Sheet - Standardized'))
    cf = pd.DataFrame(pd.read_excel(ticker, sheet_name='Cash Flow - Standardized'))

    #clean up dataframes:
    rows_inc, cols_inc = inc.shape
    rows_bal, cols_bal = bal.shape
    rows_cf, cols_cf = cf.shape

    #inc = inc_raw[3:(rows_inc - 5)]
    #bal = bal_raw[3:(rows_bal - 2)]
    #cf = cf_raw[3:(rows_cf - 5)]

    inc = inc.drop(inc.columns[[1]],axis=1)
    bal = bal.drop(bal.columns[[1]],axis=1)
    cf = cf.drop(cf.columns[[1]],axis=1)

    #inc
    iyears = pd.Series(cols_inc)
    today = 2018
    duration = (cols_inc - 2)
    i=0

    while (i  < duration):
        iyears[i+1] = today - i
        i = i + 1

    inc.columns = iyears

    #bal
    byears = pd.Series(cols_bal)
    today = 2018
    duration = (cols_bal - 2)
    i=0

    while (i  < duration):
        byears[i+1] = today - i
        i = i + 1
             
    bal.columns = byears

    #cf
    cyears = pd.Series(cols_cf)
    today = 2018
    duration = (cols_cf - 2)
    i=0

    while (i  < duration):
        cyears[i+1] = today - i
        i = i + 1
                
    cf.columns = cyears    

    inc = inc.reset_index(drop=True)
    bal = bal.reset_index(drop=True)
    cf = cf.reset_index(drop=True)

    #inc = inc.drop([inc.index[0],inc.index[2],inc.index[4],inc.index[34],inc.index[38],inc.index[40],inc.index[41],inc.index[42],inc.index[43]])
    #bal = bal.drop([bal.index[0],bal.index[1],bal.index[35],bal.index[36]])
    #cf = cf.drop([cf.index[0],cf.index[1],cf.index[15],cf.index[16],cf.index[34],cf.index[35],cf.index[47],cf.index[49]])

    inc = inc.reset_index(drop=True)
    bal = bal.reset_index(drop=True)
    cf = cf.reset_index(drop=True)

    inc_rows, inc_cols = inc.shape
    bal_rows, bal_cols = bal.shape
    cf_rows, cf_cols = cf.shape

    ticker = ticker.strip(strXlsx)
    
    #Create json object
    

    #inc.to_json('inc' + ticker + '.json', orient='records', lines=True)
    #inc.to_json('bal' + ticker + '.json', orient='records', lines=True)
    #inc.to_json('cf' + ticker + '.json', orient='records', lines=True)

    #print(inc)
    print(bal)
    print(cf)
    

#Recieve filtered json files
#sheets = pd.Series(glob.glob("*.json"))

#for i, value in sheets.iteritems():
    #if("inc" in value):
    #    print(value)
    

