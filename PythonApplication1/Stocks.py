import numpy as np
import pandas as pd 
import glob



#print 'all' to screen
pd.set_option("max_rows",2000)

#Adjust directory information
strXlsx = ".xlsx"

#Read initial xlsx files:
symbols = glob.glob("*.xlsx")

i = 0
j=0
for symbol in symbols:

	inc = pd.DataFrame(pd.read_excel(symbol, sheet_name='Income - GAAP'))
	bal = pd.DataFrame(pd.read_excel(symbol, sheet_name='Bal Sheet - Standardized'))
	cf = pd.DataFrame(pd.read_excel(symbol, sheet_name='Cash Flow - Standardized'))
	
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
	
	#for index, col in inc.itercols():
	#    print(index, str(col[3]).strip())
	#    
	ticker = JSON_r_w.importTicker(inc, bal, cf)
	
	j= j+1
	if(rows_inc < 50 ):
	    i = i + 1
	
