import numpy as np
import pandas as pd 
import json
import Reported
import inspect
import sys
import instantiate

path = './'
strXlsx = ".xlsx"
pd.set_option("max_rows",2000)

def createLocaljsonObj(symbol):
	neg =  - (sys.maxsize -1)
	data = instantiate.instantiateData()

	i = 0
	j = 0

	symXlsx = symbol + strXlsx
	inc = pd.DataFrame(pd.read_excel(symXlsx, sheet_name='Income - GAAP'))
	bal = pd.DataFrame(pd.read_excel(symXlsx, sheet_name='Bal Sheet - Standardized'))
	cf = pd.DataFrame(pd.read_excel(symXlsx, sheet_name='Cash Flow - Standardized'))
	
	rows_inc, cols_inc = inc.shape
	rows_bal, cols_bal = bal.shape
	rows_cf, cols_cf = cf.shape
	
	inc = inc[2:(rows_inc - 2)]
	bal = bal[2:(rows_bal - 2)]
	cf = cf[2:(rows_cf - 2)]
	
	inc = inc.drop(inc.columns[[1]],axis=1)
	bal = bal.drop(bal.columns[[1]],axis=1)
	cf = cf.drop(cf.columns[[1]],axis=1)

	inc = inc.drop([3], axis=0)
	bal = bal.drop([3], axis=0)
	cf = cf.drop([3], axis=0)
	
	inc = inc.reset_index(drop=True)
	bal = bal.reset_index(drop=True)
	cf = cf.reset_index(drop=True)
	
	inc.dropna(axis=0, how='all', inplace=True)
	bal.dropna(axis=0, how='all', inplace=True)
	cf.dropna(axis=0, how='all', inplace=True)
	
	inc.replace('—', neg,inplace=True)
	bal.replace('—', neg,inplace=True)
	cf.replace('—', neg,inplace=True)
	
	unkept = []
	
	symbol = symbol.strip(strXlsx)
	data['symbol'] = symbol
	index = 0
	
	#print("******************************")
	#print("INC")
	#print("******************************")
	for index, row in inc.iterrows():
		label = str(row[0].strip())
		if(Reported.inc.YEAR_INC == label):
			newRow = []
			iteryears = iter(row)
			next(iteryears)
			for year in iteryears:
				newRow.append(int(year.replace("FY", "").strip(), 10))
			Reported.ticker.YEAR_INC = applyYear(newRow)
			data['YEAR_INC'] = json.dumps(Reported.ticker.YEAR_INC)
		elif(Reported.inc.REV == label or label == Reported.fin.REV):
			Reported.ticker.REV = apply(label, row)
			data['REV'] = Reported.ticker.REV
		elif(Reported.inc.SALES_SERV_REV == label):
			Reported.ticker.SALES_SERV_REV =  apply(label, row)
			data['SALES_SERV_REV'] = Reported.ticker.SALES_SERV_REV
		elif(Reported.inc.OTHER_REV == label):	
			Reported.ticker.OTHER_REV =  apply(label, row)
			data['OTHER_REV'] = Reported.ticker.OTHER_REV
		elif(Reported.inc.COST_OF_REV == label or label == Reported.fin.COST_OF_REV):
			Reported.ticker.COST_OF_REV =  apply(label, row)
			data['COST_OF_REV'] = Reported.ticker.COST_OF_REV
		elif(Reported.inc.COGS == label):
			Reported.ticker.COGS =  apply(label, row)
			data['COGS'] = Reported.ticker.COGS
		elif(Reported.inc.PROFIT == label):
			Reported.ticker.PROFIT =  apply(label, row)
			data['PROFIT'] = Reported.ticker.PROFIT
		elif(Reported.inc.OTH_PROFIT == label):	
			Reported.ticker.OTH_PROFIT =  apply(label, row)
			data['OTH_PROFIT'] = Reported.ticker.OTH_PROFIT
		elif(Reported.inc.OP_EXP == label):	
			Reported.ticker.OP_EXP =  apply(label, row)
			data['OP_EXP'] = Reported.ticker.OP_EXP
		elif(Reported.inc.SG_AND_ADMIN == label):	
			Reported.ticker.SG_AND_ADMIN =  apply(label, row)
			data['SG_AND_ADMIN'] = Reported.ticker.SG_AND_ADMIN
		elif(Reported.inc.SELL_AND_MARK == label):
			Reported.ticker.SELL_AND_MARK =  apply(label, row)
			data['SELL_AND_MARK'] = Reported.ticker.SELL_AND_MARK
		elif(Reported.inc.GEN_AND_ADMIN == label):
			Reported.ticker.GEN_AND_ADMIN =  apply(label, row)
			data['GEN_AND_ADMIN'] = Reported.ticker.GEN_AND_ADMIN
		elif(Reported.inc.R_AND_D == label): 	
			Reported.ticker.R_AND_D =  apply(label, row)
			data['R_AND_D'] = Reported.ticker.R_AND_D
		elif(Reported.inc.DEP_AMORT == label):		
			Reported.ticker.DEP_AMORT =  apply(label, row)
			data['DEP_AMORT'] = Reported.ticker.DEP_AMORT
		elif(Reported.inc.OTH_OP_EXP == label):
			Reported.ticker.OTH_OP_EXP =  apply(label, row)
			data['OTH_OP_EXP'] = Reported.ticker.OTH_OP_EXP
		elif(Reported.inc.OP_INC_LOSS == label or label == Reported.fin.OP_INC_LOSS):	
			Reported.ticker.OP_INC_LOSS =  apply(label, row)
			data['OP_INC_LOSS'] = Reported.ticker.OP_INC_LOSS
		elif(Reported.inc.NON_OP_INC_LOSS == label):
			Reported.ticker.NON_OP_INC_LOSS =  apply(label, row)
			data['NON_OP_INC_LOSS'] = Reported.ticker.NON_OP_INC_LOSS
		elif(Reported.inc.NET_INT_EXP == label):
			Reported.ticker.NET_INT_EXP =  apply(label, row)
			data['NET_INT_EXP'] = Reported.ticker.NET_INT_EXP
		elif(Reported.inc.INT_EXP == label):		
			Reported.ticker.INT_EXP =  apply(label, row)
			data['INT_EXP'] = Reported.ticker.INT_EXP
		elif(Reported.inc.INT_INC == label):	
			Reported.ticker.INT_INC =  apply(label, row)
			data['INT_INC'] = Reported.ticker.INT_INC
		elif(Reported.inc.FOREX == label):		
			Reported.ticker.FOREX =  apply(label, row)
			data['FOREX'] = Reported.ticker.FOREX
		elif(Reported.inc.AFFILIATES == label):	
			Reported.ticker.AFFILIATES =  apply(label, row)
			data['AFFILIATES'] = Reported.ticker.AFFILIATES
		elif(Reported.inc.NON_OP_INC == label):	
			Reported.ticker.NON_OP_INC =  apply(label, row)
			data['NON_OP_INC'] = Reported.ticker.NON_OP_INC
		elif(Reported.inc.PRETAX_INCOME == label or label == Reported.fin.PRETAX_INCOME):	
			Reported.ticker.PRETAX_INCOME =  apply(label, row)
			data['PRETAX_INCOME'] = Reported.ticker.PRETAX_INCOME
		elif(Reported.inc.INC_TAX_EXPENSE == label):	
			Reported.ticker.INC_TAX_EXPENSE =  apply(label, row)
			data['INC_TAX_EXPENSE'] = Reported.ticker.INC_TAX_EXPENSE
		elif(Reported.inc.CURR_INC_TAX == label):		
			Reported.ticker.CURR_INC_TAX =  apply(label, row)
			data['CURR_INC_TAX'] = Reported.ticker.CURR_INC_TAX
		elif(Reported.inc.DEFF_INC_TAX == label):	
			Reported.ticker.DEFF_INC_TAX =  apply(label, row)
			data['DEFF_INC_TAX'] = Reported.ticker.DEFF_INC_TAX
		elif(Reported.inc.CONT_OPS == label):		
			Reported.ticker.CONT_OPS =  apply(label, row)
			data['CONT_OPS'] = Reported.ticker.CONT_OPS
		elif(Reported.inc.NET_EXTRA1 == label):	
			Reported.ticker.NET_EXTRA1 =  apply(label, row)
			data['NET_EXTRA1'] = Reported.ticker.NET_EXTRA1
		elif(Reported.inc.DISC_OPS == label):	
			Reported.ticker.DISC_OPS =  apply(label, row)
			data['DISC_OPS'] = Reported.ticker.DISC_OPS
		elif(Reported.inc.ACCT_CHNG == label):			
			Reported.ticker.ACCT_CHNG =  apply(label, row)
			data['ACCT_CHNG'] = Reported.ticker.ACCT_CHNG
		elif(Reported.inc.INCOME_MI == label):	
			Reported.ticker.INCOME_MI =  apply(label, row)
			data['INCOME_MI'] = Reported.ticker.INCOME_MI
		elif(Reported.inc.MIN_INTEREST == label):		
			Reported.ticker.MIN_INTEREST =  apply(label, row)
			data['MIN_INTEREST'] = Reported.ticker.MIN_INTEREST
		elif(Reported.inc.NI_INC == label):  	
			Reported.ticker.NI_INC =  apply(label, row)
			data['NI_INC'] = Reported.ticker.NI_INC
		elif(Reported.inc.PREF_DIVS == label):				
			Reported.ticker.PREF_DIVS =  apply(label, row)
			data['PREF_DIVS'] = Reported.ticker.PREF_DIVS
		elif(Reported.inc.OTH_ADJ == label):	
			Reported.ticker.OTH_ADJ =  apply(label, row)
			data['OTH_ADJ'] = Reported.ticker.OTH_ADJ
		elif(Reported.inc.NI_AVAIL_COMMON_GAAP == label):	
			Reported.ticker.NI_AVAIL_COMMON_GAAP =  apply(label, row)
			data['NI_AVAIL_COMMON_GAAP'] = Reported.ticker.NI_AVAIL_COMMON_GAAP
		elif(Reported.inc.NI_AVAIL_COMMON_ADJ == label):	
			Reported.ticker.NI_AVAIL_COMMON_ADJ =  apply(label, row)
			data['NI_AVAIL_COMMON_ADJ'] = Reported.ticker.NI_AVAIL_COMMON_ADJ
		elif(Reported.inc.NET_ABNORMAL == label):	
			Reported.ticker.NET_ABNORMAL =  apply(label, row)
			data['NET_ABNORMAL'] = Reported.ticker.NET_ABNORMAL
		elif(Reported.inc.NET_EXTRA2 == label):		
			Reported.ticker.NET_EXTRA2 =  apply(label, row)
			data['NET_EXTRA2'] = Reported.ticker.NET_EXTRA2
		elif(Reported.inc.BASIC_WEIGHT_AVG_SHARES == label):
			Reported.ticker.BASIC_WEIGHT_AVG_SHARES =  apply(label, row)
			data['BASIC_WEIGHT_AVG_SHARES'] = Reported.ticker.BASIC_WEIGHT_AVG_SHARES
		elif(Reported.inc.DIL_WEIGHT_AVG_SHARES == label):	
			Reported.ticker.DIL_WEIGHT_AVG_SHARES =  apply(label, row)
			data['DIL_WEIGHT_AVG_SHARES'] = Reported.ticker.DIL_WEIGHT_AVG_SHARES
		else:
			unkept.append(label)
		row = [None] * 35
	
	#print("\n\n******************************")
	#print("BAL")
	#print("******************************")
	for index, row in bal.iterrows():
		label = str(row[0].strip())
		if(Reported.bal.YEAR_BAL == label):
			newRow = []
			iteryears = iter(row)
			next(iteryears)
			for year in iteryears:
				newRow.append(int(year.replace("FY", "").strip(), 10))
			Reported.ticker.YEAR_BAL = applyYear(newRow)
			data['YEAR_BAL'] = json.dumps(Reported.ticker.YEAR_BAL)
		elif(Reported.bal.TOTAL_ASSETS1 == label):
			Reported.ticker.TOTAL_ASSETS1 = apply(label, row)
			data['TOTAL_ASSETS1'] = Reported.ticker.TOTAL_ASSETS1
		elif(Reported.bal.CASH_EQ_STI == label):
			Reported.ticker.CASH_EQ_STI = apply(label, row)
			data['CASH_EQ_STI'] = Reported.ticker.CASH_EQ_STI
		elif(Reported.bal.CASH_EQ == label):
			Reported.ticker.CASH_EQ = apply(label, row)
			data['CASH_EQ'] = Reported.ticker.CASH_EQ
		elif(Reported.bal.ST_INVEST == label):
			Reported.ticker.ST_INVEST = apply(label, row)
			data['ST_INVEST'] = Reported.ticker.ST_INVEST
		elif(Reported.bal.ACCTS_REC == label):
			Reported.ticker.ACCTS_REC = apply(label, row)
			data['ACCTS_REC'] = Reported.ticker.ACCTS_REC
		elif(Reported.bal.ACCTS_REC_NET == label):
			Reported.ticker.ACCTS_REC_NET = apply(label, row)
			data['ACCTS_REC_NET'] = Reported.ticker.ACCTS_REC_NET
		elif(Reported.bal.NOTES_REC_NET == label):
			Reported.ticker.NOTES_REC_NET = apply(label, row)
			data['NOTES_REC_NET'] = Reported.ticker.NOTES_REC_NET
		elif(Reported.bal.INV == label):
			Reported.ticker.INV = apply(label, row)
			data['INV'] = Reported.ticker.INV
		elif(Reported.bal.RAW_MAT == label):
			Reported.ticker.RAW_MAT = apply(label, row)
			data['RAW_MAT'] = Reported.ticker.RAW_MAT
		elif(Reported.bal.WIP == label):
			Reported.ticker.WIP = apply(label, row)
			data['WIP'] = Reported.ticker.WIP
		elif(Reported.bal.FIN_GOODS == label):
			Reported.ticker.FIN_GOODS = apply(label, row)
			data['FIN_GOODS'] = Reported.ticker.FIN_GOODS
		elif(Reported.bal.OTH_INV == label):
			Reported.ticker.OTH_INV = apply(label, row)
			data['OTH_INV'] = Reported.ticker.OTH_INV
		elif(Reported.bal.OTH_ST_ASSETS == label):
			Reported.ticker.OTH_ST_ASSETS = apply(label, row)
			data['OTH_ST_ASSETS'] = Reported.ticker.OTH_ST_ASSETS
		elif(Reported.bal.DERIV_HEDGE_ASSETS1 == label):
			Reported.ticker.DERIV_HEDGE_ASSETS1 = apply(label, row)
			data['DERIV_HEDGE_ASSETS1'] = Reported.ticker.DERIV_HEDGE_ASSETS1
		elif(Reported.bal.TAXES_RECIEV == label):
			Reported.ticker.TAXES_RECIEV = apply(label, row)
			data['TAXES_RECIEV'] = Reported.ticker.TAXES_RECIEV
		elif(Reported.bal.MISC_ST_ASSETS == label):
			Reported.ticker.MISC_ST_ASSETS = apply(label, row)
			data['MISC_ST_ASSETS'] = Reported.ticker.MISC_ST_ASSETS
		elif(Reported.bal.TOTAL_CURR_ASSETS == label):
			Reported.ticker.TOTAL_CURR_ASSETS = apply(label, row)
			data['TOTAL_CURR_ASSETS'] = Reported.ticker.TOTAL_CURR_ASSETS
		elif(Reported.bal.PPE_NET == label):
			Reported.ticker.PPE_NET = apply(label, row)
			data['PPE_NET'] = Reported.ticker.PPE_NET
		elif(Reported.bal.PPE == label):
			Reported.ticker.PPE = apply(label, row)
			data['PPE'] = Reported.ticker.PPE
		elif(Reported.bal.ACC_DEPREC == label):
			Reported.ticker.ACC_DEPREC = apply(label, row)
			data['ACC_DEPREC'] = Reported.ticker.ACC_DEPREC
		elif(Reported.bal.LTI_RECEIVABLES == label):
			Reported.ticker.LTI_RECEIVABLES = apply(label, row)
			data['LTI_RECEIVABLES'] = Reported.ticker.LTI_RECEIVABLES
		elif(Reported.bal.LT_INVEST == label):
			Reported.ticker.LT_INVEST = apply(label, row)
			data['LT_INVEST'] = Reported.ticker.LT_INVEST
		elif(Reported.bal.OTH_LT_ASSETS == label):
			Reported.ticker.OTH_LT_ASSETS = apply(label, row)
			data['OTH_LT_ASSETS'] = Reported.ticker.OTH_LT_ASSETS
		elif(Reported.bal.TOTAL_INTANG_ASSETS == label):
			Reported.ticker.TOTAL_INTANG_ASSETS = apply(label, row)
			data['TOTAL_INTANG_ASSETS'] = Reported.ticker.TOTAL_INTANG_ASSETS
		elif(Reported.bal.GOODWILL == label):
			Reported.ticker.GOODWILL = apply(label, row)
			data['GOODWILL'] = Reported.ticker.GOODWILL
		elif(Reported.bal.OTH_INTANG_ASSETS == label):
			Reported.ticker.OTH_INTANG_ASSETS = apply(label, row)
			data['OTH_INTANG_ASSETS'] = Reported.ticker.OTH_INTANG_ASSETS
		elif(Reported.bal.PREPAID_EXP == label):
			Reported.ticker.PREPAID_EXP = apply(label, row)
			data['PREPAID_EXP'] = Reported.ticker.PREPAID_EXP
		elif(Reported.bal.DEFF_TAX_ASSETS == label):
			Reported.ticker.DEFF_TAX_ASSETS = apply(label, row)
			data['DEFF_TAX_ASSETS'] = Reported.ticker.DEFF_TAX_ASSETS
		elif(Reported.bal.DERIV_HEDGE_ASSETS2 == label):
			Reported.ticker.DERIV_HEDGE_ASSETS2 = apply(label, row)
			data['DERIV_HEDGE_ASSETS2'] = Reported.ticker.DERIV_HEDGE_ASSETS2
		elif(Reported.bal.MISC_ASSETS == label):
			Reported.ticker.MISC_ASSETS = apply(label, row)
			data['MISC_ASSETS'] = Reported.ticker.MISC_ASSETS
		elif(Reported.bal.TOTAL_NON_CURR_ASSETS == label):
			Reported.ticker.TOTAL_NON_CURR_ASSETS = apply(label, row)
			data['TOTAL_NON_CURR_ASSETS'] = Reported.ticker.TOTAL_NON_CURR_ASSETS
		elif(Reported.bal.TOTAL_ASSETS2 == label):
			Reported.ticker.TOTAL_ASSETS2 = apply(label, row)
			data['TOTAL_ASSETS2'] = Reported.ticker.TOTAL_ASSETS2
		elif(Reported.bal.PAYABLES_ACCRUALS == label):
			Reported.ticker.PAYABLES_ACCRUALS = apply(label, row)
			data['PAYABLES_ACCRUALS'] = Reported.ticker.PAYABLES_ACCRUALS
		elif(Reported.bal.PAYABLES == label):
			Reported.ticker.PAYABLES = apply(label, row)
			data['PAYABLES'] = Reported.ticker.PAYABLES
		elif(Reported.bal.ACCRUED_TAXES == label):
			Reported.ticker.ACCRUED_TAXES = apply(label, row)
			data['ACCRUED_TAXES'] = Reported.ticker.ACCRUED_TAXES
		elif(Reported.bal.INT_DIVS_PAYABLES == label):
			Reported.ticker.INT_DIVS_PAYABLES = apply(label, row)
			data['INT_DIVS_PAYABLES'] = Reported.ticker.INT_DIVS_PAYABLES
		elif(Reported.bal.OTH_PAYABLES_ACCURALS == label):
			Reported.ticker.OTH_PAYABLES_ACCURALS = apply(label, row)
			data['OTH_PAYABLES_ACCURALS'] = Reported.ticker.OTH_PAYABLES_ACCURALS
		elif(Reported.bal.ST_DEBT == label):
			Reported.ticker.ST_DEBT = apply(label, row)
			data['ST_DEBT'] = Reported.ticker.ST_DEBT
		elif(Reported.bal.ST_BORROWINGS == label):
			Reported.ticker.ST_BORROWINGS = apply(label, row)
			data['ST_BORROWINGS'] = Reported.ticker.ST_BORROWINGS
		elif(Reported.bal.ST_FIN_LEASES == label):
			Reported.ticker.ST_FIN_LEASES = apply(label, row)
			data['ST_FIN_LEASES'] = Reported.ticker.ST_FIN_LEASES
		elif(Reported.bal.ST_OP_LEASES == label):
			Reported.ticker.ST_OP_LEASES = apply(label, row)
			data['ST_OP_LEASES'] = Reported.ticker.ST_OP_LEASES
		elif(Reported.bal.CURR_LT_DEBT == label):
			Reported.ticker.CURR_LT_DEBT = apply(label, row)
			data['CURR_LT_DEBT'] = Reported.ticker.CURR_LT_DEBT
		elif(Reported.bal.OTH_ST_LIAB == label):
			Reported.ticker.OTH_ST_LIAB = apply(label, row)
			data['OTH_ST_LIAB'] = Reported.ticker.OTH_ST_LIAB
		elif(Reported.bal.DEFF_REV_1 == label):
			Reported.ticker.DEFF_REV_1 = apply(label, row)
			data['DEFF_REV_1'] = Reported.ticker.DEFF_REV_1
		elif(Reported.bal.DERIV_HEDGE_1 == label):
			Reported.ticker.DERIV_HEDGE_1 = apply(label, row)
			data['DERIV_HEDGE_1'] = Reported.ticker.DERIV_HEDGE_1
		elif(Reported.bal.MISC_ST_LIAB == label):
			Reported.ticker.MISC_ST_LIAB = apply(label, row)
			data['MISC_ST_LIAB'] = Reported.ticker.MISC_ST_LIAB
		elif(Reported.bal.TOTAL_CURR_LIAB == label):
			Reported.ticker.TOTAL_CURR_LIAB = apply(label, row)
			data['TOTAL_CURR_LIAB'] = Reported.ticker.TOTAL_CURR_LIAB
		elif(Reported.bal.LT_DEBT == label):
			Reported.ticker.LT_DEBT = apply(label, row)
			data['LT_DEBT'] = Reported.ticker.LT_DEBT
		elif(Reported.bal.LT_BORROW == label):
			Reported.ticker.LT_BORROW = apply(label, row)
			data['LT_BORROW'] = Reported.ticker.LT_BORROW
		elif(Reported.bal.LT_FIN_LEASES == label):
			Reported.ticker.LT_FIN_LEASES = apply(label, row)
			data['LT_FIN_LEASES'] = Reported.ticker.LT_FIN_LEASES
		elif(Reported.bal.LT_OP_LEASES == label):
			Reported.ticker.LT_OP_LEASES = apply(label, row)
			data['LT_OP_LEASES'] = Reported.ticker.LT_OP_LEASES
		elif(Reported.bal.OTH_LT_LIAB == label):
			Reported.ticker.OTH_LT_LIAB = apply(label, row)
			data['OTH_LT_LIAB'] = Reported.ticker.OTH_LT_LIAB
		elif(Reported.bal.ACCURED_LIAB == label):
			Reported.ticker.ACCURED_LIAB = apply(label, row)
			data['ACCURED_LIAB'] = Reported.ticker.ACCURED_LIAB
		elif(Reported.bal.PENSION_LIAB == label):
			Reported.ticker.PENSION_LIAB = apply(label, row)
			data['PENSION_LIAB'] = Reported.ticker.PENSION_LIAB
		elif(Reported.bal.OTH_POST_RET_BEN == label):
			Reported.ticker.OTH_POST_RET_BEN = apply(label, row)
			data['OTH_POST_RET_BEN'] = Reported.ticker.OTH_POST_RET_BEN
		elif(Reported.bal.PENSIONS == label):
			Reported.ticker.PENSIONS = apply(label, row)
			data['PENSIONS'] = Reported.ticker.PENSIONS
		elif(Reported.bal.DEFF_REV_2 == label):
			Reported.ticker.DEFF_REV_2 = apply(label, row)
			data['DEFF_REV_2'] = Reported.ticker.DEFF_REV_2
		elif(Reported.bal.DEF_TAX_LIAB == label):
			Reported.ticker.DEF_TAX_LIAB = apply(label, row)
			data['DEF_TAX_LIAB'] = Reported.ticker.DEF_TAX_LIAB
		elif(Reported.bal.DERIV_HEDGE_2 == label):
			Reported.ticker.DERIV_HEDGE_2 = apply(label, row)
			data['DERIV_HEDGE_2'] = Reported.ticker.DERIV_HEDGE_2
		elif(Reported.bal.MISC_LT_LIAB == label):
			Reported.ticker.MISC_LT_LIAB = apply(label, row)
			data['MISC_LT_LIAB'] = Reported.ticker.MISC_LT_LIAB
		elif(Reported.bal.TOTAL_NON_CURR_LIAB == label):
			Reported.ticker.TOTAL_NON_CURR_LIAB = apply(label, row)
			data['TOTAL_NON_CURR_LIAB'] = Reported.ticker.TOTAL_NON_CURR_LIAB
		elif(Reported.bal.TOTAL_LIAB == label):
			Reported.ticker.TOTAL_LIAB = apply(label, row)
			data['TOTAL_LIAB'] = Reported.ticker.TOTAL_LIAB
		elif(Reported.bal.PREF_EQUITY_HYBRID_CAP == label):
			Reported.ticker.PREF_EQUITY_HYBRID_CAP = apply(label, row)
			data['PREF_EQUITY_HYBRID_CAP'] = Reported.ticker.PREF_EQUITY_HYBRID_CAP
		elif(Reported.bal.SHARE_CAP_APIC == label):
			Reported.ticker.SHARE_CAP_APIC = apply(label, row)
			data['SHARE_CAP_APIC'] = Reported.ticker.SHARE_CAP_APIC
		elif(Reported.bal.COMMON_STOCK == label):
			Reported.ticker.COMMON_STOCK = apply(label, row)
			data['COMMON_STOCK'] = Reported.ticker.COMMON_STOCK
		elif(Reported.bal.ADD_PAID_CAP == label):
			Reported.ticker.ADD_PAID_CAP = apply(label, row)
			data['ADD_PAID_CAP'] = Reported.ticker.ADD_PAID_CAP
		elif(Reported.bal.TREASURY_STOCK == label):
			Reported.ticker.TREASURY_STOCK = apply(label, row)
			data['TREASURY_STOCK'] = Reported.ticker.TREASURY_STOCK
		elif(Reported.bal.RE == label):
			Reported.ticker.RE = apply(label, row)
			data['RE'] = Reported.ticker.RE
		elif(Reported.bal.OTH_EQUITY == label):
			Reported.ticker.OTH_EQUITY = apply(label, row)
			data['OTH_EQUITY'] = Reported.ticker.OTH_EQUITY
		elif(Reported.bal.EQUITY_BEFORE_MIN_INT == label):
			Reported.ticker.EQUITY_BEFORE_MIN_INT = apply(label, row)
			data['EQUITY_BEFORE_MIN_INT'] = Reported.ticker.EQUITY_BEFORE_MIN_INT
		elif(Reported.bal.MIN_NON_CONTROL_INT == label):
			Reported.ticker.MIN_NON_CONTROL_INT = apply(label, row)
			data['MIN_NON_CONTROL_INT'] = Reported.ticker.MIN_NON_CONTROL_INT
		elif(Reported.bal.TOTAL_EQUITY == label):
			Reported.ticker.TOTAL_EQUITY = apply(label, row)
			data['TOTAL_EQUITY'] = Reported.ticker.TOTAL_EQUITY
		elif(Reported.bal.LIAB_AND_EQUITY == label):
			Reported.ticker.LIAB_AND_EQUITY = apply(label, row)
			data['LIAB_AND_EQUITY'] = Reported.ticker.LIAB_AND_EQUITY
		else:
			unkept.append(label)
		row = [None] * 35
	
	#print("\n\n******************************")
	#print("CF")
	#print("******************************")
	for index, row in cf.iterrows():
		label = str(row[0].strip())
		if(Reported.cf.YEAR_CF == label):
			newRow = []
			iteryears = iter(row)
			next(iteryears)
			for year in iteryears:
				newRow.append(int(year.replace("FY", "").strip(), 10))
			Reported.ticker.YEAR_CF = applyYear(newRow)
			data['YEAR_CF'] = json.dumps(Reported.ticker.YEAR_CF)
		elif(Reported.cf.NI_CF == label):
			Reported.ticker.NI_CF = apply(label, row)
			data['NI_CF'] = Reported.ticker.NI_CF
		elif(Reported.cf.DEPRE_AMORT == label):
			Reported.ticker.DEPRE_AMORT = apply(label, row)
			data['DEPRE_AMORT'] = Reported.ticker.DEPRE_AMORT
		elif(Reported.cf.NON_CASH_ITEMS == label):
			Reported.ticker.NON_CASH_ITEMS = apply(label, row)
			data['NON_CASH_ITEMS'] = Reported.ticker.NON_CASH_ITEMS
		elif(Reported.cf.STOCK_COMP == label):
			Reported.ticker.STOCK_COMP = apply(label, row)
			data['STOCK_COMP'] = Reported.ticker.STOCK_COMP
		elif(Reported.cf.DEF_INT_COMP == label):
			Reported.ticker.DEF_INT_COMP = apply(label, row)
			data['DEF_INT_COMP'] = Reported.ticker.DEF_INT_COMP
		elif(Reported.cf.OTH_NON_CASH_ADJ == label):
			Reported.ticker.OTH_NON_CASH_ADJ = apply(label, row)
			data['OTH_NON_CASH_ADJ'] = Reported.ticker.OTH_NON_CASH_ADJ
		elif(Reported.cf.CHG_NON_CASH_OP == label):
			Reported.ticker.CHG_NON_CASH_OP = apply(label, row)
			data['CHG_NON_CASH_OP'] = Reported.ticker.CHG_NON_CASH_OP
		elif(Reported.cf.CREDIT_SALES == label):
			Reported.ticker.CREDIT_SALES = apply(label, row)
			data['CREDIT_SALES'] = Reported.ticker.CREDIT_SALES
		elif(Reported.cf.CHG_INVENTORIES == label):
			Reported.ticker.CHG_INVENTORIES = apply(label, row)
			data['CHG_INVENTORIES'] = Reported.ticker.CHG_INVENTORIES
		elif(Reported.cf.CHG_ACCTS_PAYABLE == label):
			Reported.ticker.CHG_ACCTS_PAYABLE = apply(label, row)
			data['CHG_ACCTS_PAYABLE'] = Reported.ticker.CHG_ACCTS_PAYABLE
		elif(Reported.cf.CHG_OTHER == label):
			Reported.ticker.CHG_OTHER = apply(label, row)
			data['CHG_OTHER'] = Reported.ticker.CHG_OTHER
		elif(Reported.cf.NET_CASH_DISC_OPS1 == label):
			Reported.ticker.NET_CASH_DISC_OPS1 = apply(label, row)
			data['NET_CASH_DISC_OPS1'] = Reported.ticker.NET_CASH_DISC_OPS1
		elif(Reported.cf.CASH_OP_ACT == label):
			Reported.ticker.CASH_OP_ACT = apply(label, row)
			data['CASH_OP_ACT'] = Reported.ticker.CASH_OP_ACT
		elif(Reported.cf.CASH_INVEST_ACT1 == label):
			Reported.ticker.CASH_INVEST_ACT1 = apply(label, row)
			data['CASH_INVEST_ACT1'] = Reported.ticker.CASH_INVEST_ACT1
		elif(Reported.cf.CHG_FIXED_INTANG == label):
			Reported.ticker.CHG_FIXED_INTANG = apply(label, row)
			data['CHG_FIXED_INTANG'] = Reported.ticker.CHG_FIXED_INTANG
		elif(Reported.cf.DISP_FIXED_INTANG == label):
			Reported.ticker.DISP_FIXED_INTANG = apply(label, row)
			data['DISP_FIXED_INTANG'] = Reported.ticker.DISP_FIXED_INTANG
		elif(Reported.cf.DISP_FIXED_PROD_ASSETS == label):
			Reported.ticker.DISP_FIXED_PROD_ASSETS = apply(label, row)
			data['DISP_FIXED_PROD_ASSETS'] = Reported.ticker.DISP_FIXED_PROD_ASSETS
		elif(Reported.cf.DISP_INTANG_ASSETS == label):
			Reported.ticker.DISP_INTANG_ASSETS = apply(label, row)
			data['DISP_INTANG_ASSETS'] = Reported.ticker.DISP_INTANG_ASSETS
		elif(Reported.cf.ACQ_FIXED_INTANG == label):
			Reported.ticker.ACQ_FIXED_INTANG = apply(label, row)
			data['ACQ_FIXED_INTANG'] = Reported.ticker.ACQ_FIXED_INTANG
		elif(Reported.cf.ACQ_FIXED_PROD_ASSETS == label):
			Reported.ticker.ACQ_FIXED_PROD_ASSETS = apply(label, row)
			data['ACQ_FIXED_PROD_ASSETS'] = Reported.ticker.ACQ_FIXED_PROD_ASSETS
		elif(Reported.cf.ACQ_INTANG_ASSETS == label):
			Reported.ticker.ACQ_INTANG_ASSETS = apply(label, row)
			data['ACQ_INTANG_ASSETS'] = Reported.ticker.ACQ_INTANG_ASSETS
		elif(Reported.cf.NET_CHG_LT_INVEST == label):
			Reported.ticker.NET_CHG_LT_INVEST = apply(label, row)
			data['NET_CHG_LT_INVEST'] = Reported.ticker.NET_CHG_LT_INVEST
		elif(Reported.cf.DEC_LT_INVEST == label):
			Reported.ticker.DEC_LT_INVEST = apply(label, row)
			data['DEC_LT_INVEST'] = Reported.ticker.DEC_LT_INVEST
		elif(Reported.cf.INC_LT_INVEST == label):
			Reported.ticker.INC_LT_INVEST = apply(label, row)
			data['INC_LT_INVEST'] = Reported.ticker.INC_LT_INVEST
		elif(Reported.cf.NET_CASH_ACQ_DIV == label):
			Reported.ticker.NET_CASH_ACQ_DIV = apply(label, row)
			data['NET_CASH_ACQ_DIV'] = Reported.ticker.NET_CASH_ACQ_DIV
		elif(Reported.cf.CASH_DIVEST == label):
			Reported.ticker.CASH_DIVEST = apply(label, row)
			data['CASH_DIVEST'] = Reported.ticker.CASH_DIVEST
		elif(Reported.cf.CASH_ACQ_SUBS == label):
			Reported.ticker.CASH_ACQ_SUBS = apply(label, row)
			data['CASH_ACQ_SUBS'] = Reported.ticker.CASH_ACQ_SUBS
		elif(Reported.cf.CASH_JVS == label):
			Reported.ticker.CASH_JVS = apply(label, row)
			data['CASH_JVS'] = Reported.ticker.CASH_JVS
		elif(Reported.cf.OTH_INVEST_ACT == label):
			Reported.ticker.OTH_INVEST_ACT = apply(label, row)
			data['OTH_INVEST_ACT'] = Reported.ticker.OTH_INVEST_ACT
		elif(Reported.cf.NET_CASH_DISC_OPS2 == label):
			Reported.ticker.NET_CASH_DISC_OPS2 = apply(label, row)
			data['NET_CASH_DISC_OPS2'] = Reported.ticker.NET_CASH_DISC_OPS2
		elif(Reported.cf.CASH_INVEST == label):
			Reported.ticker.CASH_INVEST = apply(label, row)
			data['CASH_INVEST'] = Reported.ticker.CASH_INVEST
		elif(Reported.cf.CASH_FIN_ACT2 == label):
			Reported.ticker.CASH_FIN_ACT2 = apply(label, row)
			data['CASH_FIN_ACT2'] = Reported.ticker.CASH_FIN_ACT2
		elif(Reported.cf.DIVS_PAID == label):
			Reported.ticker.DIVS_PAID = apply(label, row)
			data['DIVS_PAID'] = Reported.ticker.DIVS_PAID
		elif(Reported.cf.CASH_REPAY_DEBT == label):
			Reported.ticker.CASH_REPAY_DEBT = apply(label, row)
			data['CASH_REPAY_DEBT'] = Reported.ticker.CASH_REPAY_DEBT
		elif(Reported.cf.CASH_ST_DEBT == label):
			Reported.ticker.CASH_ST_DEBT = apply(label, row)
			data['CASH_ST_DEBT'] = Reported.ticker.CASH_ST_DEBT
		elif(Reported.cf.CASH_LT_DEBT == label):
			Reported.ticker.CASH_LT_DEBT = apply(label, row)
			data['CASH_LT_DEBT'] = Reported.ticker.CASH_LT_DEBT
		elif(Reported.cf.REPAY_LT_DEBT == label):
			Reported.ticker.REPAY_LT_DEBT = apply(label, row)
			data['REPAY_LT_DEBT'] = Reported.ticker.REPAY_LT_DEBT
		elif(Reported.cf.CASH_REPURCH_EQUITY == label):
			Reported.ticker.CASH_REPURCH_EQUITY = apply(label, row)
			data['CASH_REPURCH_EQUITY'] = Reported.ticker.CASH_REPURCH_EQUITY
		elif(Reported.cf.INC_CAPITAL_STOCK == label):
			Reported.ticker.INC_CAPITAL_STOCK = apply(label, row)
			data['INC_CAPITAL_STOCK'] = Reported.ticker.INC_CAPITAL_STOCK
		elif(Reported.cf.DEC_CAPITAL_STOCK == label):
			Reported.ticker.DEC_CAPITAL_STOCK = apply(label, row)
			data['DEC_CAPITAL_STOCK'] = Reported.ticker.DEC_CAPITAL_STOCK
		elif(Reported.cf.OTH_FIN_ACT == label):
			Reported.ticker.OTH_FIN_ACT = apply(label, row)
			data['OTH_FIN_ACT'] = Reported.ticker.OTH_FIN_ACT
		elif(Reported.cf.NET_CASH_DISC_OPS3 == label):
			Reported.ticker.NET_CASH_DISC_OPS3 = apply(label, row)
			data['NET_CASH_DISC_OPS3'] = Reported.ticker.NET_CASH_DISC_OPS3
		elif(Reported.cf.CASH_FIN_ACT2 == label):
			Reported.ticker.CASH_FIN_ACT2 = apply(label, row)
			data['CASH_FIN_ACT2'] = Reported.ticker.CASH_FIN_ACT2
		elif(Reported.cf.EFFECT_FOREX_RATES == label):
			Reported.ticker.EFFECT_FOREX_RATES = apply(label, row)
			data['EFFECT_FOREX_RATES'] = Reported.ticker.EFFECT_FOREX_RATES
		elif(Reported.cf.NET_CHG_CASH == label):
			Reported.ticker.NET_CHG_CASH = apply(label, row)
			data['NET_CHG_CASH'] = Reported.ticker.NET_CHG_CASH
		elif(Reported.cf.CASH_PAID_TAXES == label):
			Reported.ticker.CASH_PAID_TAXES = apply(label, row)
			data['CASH_PAID_TAXES'] = Reported.ticker.CASH_PAID_TAXES
		elif(Reported.cf.CASH_PAID_INT == label):
			Reported.ticker.CASH_PAID_INT = apply(label, row)
			data['CASH_PAID_INT'] = Reported.ticker.CASH_PAID_INT
		else:
			unkept.append(label)
		row = [None] * 35

	filename = symbol.strip(strXlsx)
	ToFile(path, filename, data)
	decorateFile(path, filename + ".json" )
	getTickerObject()



def getTickerObject():
	omit = "as_integer_ratio", "conjugate", "fromhex", "hex", "imag", "is_integer", "real"
	#print([x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ])
	return [x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ]


			
			

def ToFile(path, fileName, data):
	filePathNameExt = './' + path + '/' + fileName + '.json'
	
	with open(filePathNameExt, 'w') as fp:
		json.dump(data, fp)




def decorateFile(path, fileName):

	myfile = open(fileName, "r+")
	contents = myfile.read()        
	contents = contents.replace('nan', 'null').replace('None', 'null').replace('-2147483646', 'null').replace('\"\\\"[', '[').replace(']\\\"\"', ']')
	contents = contents.replace('\"[', '[').replace(']\"', ']').replace('\\\"', '\'').replace('Shareholders\'', 'Shareholders')
	contents = contents.replace('\'', '\"')
	newFile = open(fileName, "w")
	newFile.write(contents)        
	myfile.close()               
	newFile.close()  


def apply(label, row):
	newRow = [None] * 35
	newRow[0] = label
	i=1
	while(i < len(row)):
		newRow[i] = row[i]
		i += 1
		
	return str(newRow)

def applyYear(row):
	newRow = [None] * 35
	newRow[0] = "Year"
	i=0
	while(i < len(row)):
		newRow[i+1] = str(row[i])
		i += 1
		
	return newRow

