import numpy as np
import pandas as pd 
import glob
import os
import json
import re
import Reported
import pprint

#Read initial xlsx files:
#symbols = glob.glob("*.xlsx")
symbol = "GOOGL.xlsx"
i = 0
j=0
#for symbol in symbols:

inc = pd.DataFrame(pd.read_excel(symbol, sheet_name='Income - GAAP'))
bal = pd.DataFrame(pd.read_excel(symbol, sheet_name='Bal Sheet - Standardized'))
cf = pd.DataFrame(pd.read_excel(symbol, sheet_name='Cash Flow - Standardized'))

rows_inc, cols_inc = inc.shape
rows_bal, cols_bal = bal.shape
rows_cf, cols_cf = cf.shape

inc = inc[3:(rows_inc - 2)]
bal = bal[3:(rows_bal - 2)]
cf = cf[3:(rows_cf - 2)]

inc = inc.drop(inc.columns[[1]],axis=1)
bal = bal.drop(bal.columns[[1]],axis=1)
cf = cf.drop(cf.columns[[1]],axis=1)

inc = inc.reset_index(drop=True)
bal = bal.reset_index(drop=True)
cf = cf.reset_index(drop=True)

inc.dropna(axis=0, how='all', inplace=True)
bal.dropna(axis=0, how='all', inplace=True)
cf.dropna(axis=0, how='all', inplace=True)

unkept = []

print("******************************")
print("INC")
print("******************************")
for index, row in inc.iterrows():
	label =  str(row[0].strip())
	if(Reported.inc.REV == label ):
		Reported.ticker.REV = row
		Reported.ticker.REV[0] = label
	elif(Reported.inc.SALES_SERV_REV == label ):
		Reported.ticker.SALES_SERV_REV = row
		Reported.ticker.SALES_SERV_REV[0] = label
	elif(Reported.inc.OTHER_REV == label ):	
		Reported.ticker.OTHER_REV = row
		Reported.ticker.OTHER_REV[0] = label
	elif(Reported.inc.COST_OF_REV == label ):
		Reported.ticker.COST_OF_REV = row
		Reported.ticker.COST_OF_REV[0] = label
	elif(Reported.inc.COGS == label ):
		Reported.ticker.COGS = row
		Reported.ticker.COGS[0] = label
	elif(Reported.inc.PROFIT == label ):
		Reported.ticker.PROFIT = row
		Reported.ticker.PROFIT[0] = label
	elif(Reported.inc.OTH_PROFIT == label ):	
		Reported.ticker.OTH_PROFIT = row
		Reported.ticker.OTH_PROFIT[0] = label
	elif(Reported.inc.OP_EXP == label ):	
		Reported.ticker.OP_EXP = row
		Reported.ticker.OP_EXP[0] = label
	elif(Reported.inc.SG_AND_ADMIN == label ):	
		Reported.ticker.SG_AND_ADMIN = row
		Reported.ticker.SG_AND_ADMIN[0] = label
	elif(Reported.inc.SELL_AND_MARK == label ):
		Reported.ticker.SELL_AND_MARK = row
		Reported.ticker.SELL_AND_MARK[0] = label
	elif(Reported.inc.GEN_AND_ADMIN == label ):
		Reported.ticker.GEN_AND_ADMIN = row
		Reported.ticker.GEN_AND_ADMIN[0] = label
	elif(Reported.inc.R_AND_D == label ): 	
		Reported.ticker.R_AND_D = row
		Reported.ticker.R_AND_D[0] = label
	elif(Reported.inc.DEP_AMORT == label ):		
		Reported.ticker.DEP_AMORT = row
		Reported.ticker.DEP_AMORT[0] = label
	elif(Reported.inc.OTH_OP_EXP == label ):
		Reported.ticker.OTH_OP_EXP = row
		Reported.ticker.OTH_OP_EXP[0] = label
	elif(Reported.inc.OP_INC_LOSS == label ):	
		Reported.ticker.OP_INC_LOSS = row
		Reported.ticker.OP_INC_LOSS[0] = label
	elif(Reported.inc.NON_OP_INC_LOSS == label ):
		Reported.ticker.NON_OP_INC_LOSS = row
		Reported.ticker.NON_OP_INC_LOSS[0] = label
	elif(Reported.inc.NET_INT_EXP == label ):
		Reported.ticker.NET_INT_EXP = row
		Reported.ticker.NET_INT_EXP[0] = label
	elif(Reported.inc.INT_EXP == label ):		
		Reported.ticker.INT_EXP = row
		Reported.ticker.INT_EXP[0] = label
	elif(Reported.inc.INT_INC == label ):	
		Reported.ticker.INT_INC = row
		Reported.ticker.INT_INC[0] = label
	elif(Reported.inc.FOREX == label ):		
		Reported.ticker.FOREX = row
		Reported.ticker.FOREX[0] = label
	elif(Reported.inc.AFFILIATES == label ):	
		Reported.ticker.AFFILIATES = row
		Reported.ticker.AFFILIATES[0] = label
	elif(Reported.inc.NON_OP_INC == label ):	
		Reported.ticker.NON_OP_INC = row
		Reported.ticker.NON_OP_INC[0] = label
	elif(Reported.inc.PRETAX_INCOME == label ):	
		Reported.ticker.PRETAX_INCOME = row
		Reported.ticker.PRETAX_INCOME[0] = label
	elif(Reported.inc.INC_TAX_BENEFIT == label ):	
		Reported.ticker.INC_TAX_BENEFIT = row
		Reported.ticker.INC_TAX_BENEFIT[0] = label
	elif(Reported.inc.CURR_INC_TAX == label ):		
		Reported.ticker.CURR_INC_TAX = row
		Reported.ticker.CURR_INC_TAX[0] = label
	elif(Reported.inc.DEFF_INC_TAX == label ):	
		Reported.ticker.DEFF_INC_TAX = row
		Reported.ticker.DEFF_INC_TAX[0] = label
	elif(Reported.inc.CONT_OPS == label ):		
		Reported.ticker.CONT_OPS = row
		Reported.ticker.CONT_OPS[0] = label
	elif(Reported.inc.NET_EXTRA1 == label ):	
		Reported.ticker.NET_EXTRA1 = row
		Reported.ticker.NET_EXTRA1[0] = label
	elif(Reported.inc.DISC_OPS == label ):	
		Reported.ticker.DISC_OPS = row
		Reported.ticker.DISC_OPS[0] = label
	elif(Reported.inc.ACCT_CHNG == label ):			
		Reported.ticker.ACCT_CHNG = row
		Reported.ticker.ACCT_CHNG[0] = label
	elif(Reported.inc.INCOME_MI == label ):	
		Reported.ticker.INCOME_MI = row
		Reported.ticker.INCOME_MI[0] = label
	elif(Reported.inc.MIN_INTEREST == label ):		
		Reported.ticker.MIN_INTEREST = row
		Reported.ticker.MIN_INTEREST[0] = label
	elif(Reported.inc.NI_INC == label ):  	
		Reported.ticker.NI_INC = row
		Reported.ticker.NI_INC[0] = label
	elif(Reported.inc.PREF_DIVS == label ):				
		Reported.ticker.PREF_DIVS = row
		Reported.ticker.PREF_DIVS[0] = label
	elif(Reported.inc.OTH_ADJ == label ):	
		Reported.ticker.OTH_ADJ = row
		Reported.ticker.OTH_ADJ[0] = label
	elif(Reported.inc.NI_AVAIL_COMMON_GAAP == label ):	
		Reported.ticker.NI_AVAIL_COMMON_GAAP = row
		Reported.ticker.NI_AVAIL_COMMON_GAAP[0] = label
	elif(Reported.inc.NI_AVAIL_COMMON_ADJ == label ):	
		Reported.ticker.NI_AVAIL_COMMON_ADJ = row
		Reported.ticker.NI_AVAIL_COMMON_ADJ[0] = label
	elif(Reported.inc.NET_ABNORMAL == label ):	
		Reported.ticker.NET_ABNORMAL = row
		Reported.ticker.NET_ABNORMAL[0] = label
	elif(Reported.inc.NET_EXTRA2 == label ):		
		Reported.ticker.NET_EXTRA2 = row
		Reported.ticker.NET_EXTRA2[0] = label
	elif(Reported.inc.BASIC_WEIGHT_AVG_SHARES == label ):
		Reported.ticker.BASIC_WEIGHT_AVG_SHARES = row
		Reported.ticker.BASIC_WEIGHT_AVG_SHARES[0] = label
	elif(Reported.inc.DIL_WEIGHT_AVG_SHARES == label ):	
		Reported.ticker.DIL_WEIGHT_AVG_SHARES = row
		Reported.ticker.DIL_WEIGHT_AVG_SHARES[0] = label
	else:
		unkept.append(label)

print("\n\n******************************")
print("BAL")
print("******************************")
for index, row in bal.iterrows():
	if(Reported.bal.TOTAL_ASSETS1 == label ):
		Reported.ticker.TOTAL_ASSETS1 = row
		Reported.ticker.TOTAL_ASSETS1[0] = label
	elif(Reported.bal.CASH_EQ_STI == label ):
		Reported.ticker.CASH_EQ_STI = row
		Reported.ticker.CASH_EQ_STI[0] = label
	elif(Reported.bal.CASH_EQ == label ):
		Reported.ticker.CASH_EQ = row
		Reported.ticker.CASH_EQ[0] = label
	elif(Reported.bal.STI == label ):
		Reported.ticker.STI = row
		Reported.ticker.STI[0] = label
	elif(Reported.bal.ACCTS_REC == label ):
		Reported.ticker.ACCTS_REC = row
		Reported.ticker.ACCTS_REC[0] = label
	elif(Reported.bal.ACCTS_REC_NET == label ):
		Reported.ticker.ACCTS_REC_NET = row
		Reported.ticker.ACCTS_REC_NET[0] = label
	elif(Reported.bal.NOTES_REC_NET == label ):
		Reported.ticker.NOTES_REC_NET = row
		Reported.ticker.NOTES_REC_NET[0] = label
	elif(Reported.bal.INV == label ):
		Reported.ticker.INV = row
		Reported.ticker.INV[0] = label
	elif(Reported.bal.RAW_MAT == label ):
		Reported.ticker.RAW_MAT = row
		Reported.ticker.RAW_MAT[0] = label
	elif(Reported.bal.WIP == label ):
		Reported.ticker.WIP = row
		Reported.ticker.WIP[0] = label
	elif(Reported.bal.FIN_GOODS == label ):
		Reported.ticker.FIN_GOODS = row
		Reported.ticker.FIN_GOODS[0] = label
	elif(Reported.bal.OTH_INV == label ):
		Reported.ticker.OTH_INV = row
		Reported.ticker.OTH_INV[0] = label
	elif(Reported.bal.OTH_ST_ASSETS == label ):
		Reported.ticker.OTH_ST_ASSETS = row
		Reported.ticker.OTH_ST_ASSETS[0] = label
	elif(Reported.bal.DERIV_HEDGE_ASSETS1 == label ):
		Reported.ticker.DERIV_HEDGE_ASSETS1 = row
		Reported.ticker.DERIV_HEDGE_ASSETS1[0] = label
	elif(Reported.bal.TAXES_RECIEV == label ):
		Reported.ticker.TAXES_RECIEV = row
		Reported.ticker.TAXES_RECIEV[0] = label
	elif(Reported.bal.MISC_ST_ASSETS == label ):
		Reported.ticker.MISC_ST_ASSETS = row
		Reported.ticker.MISC_ST_ASSETS[0] = label
	elif(Reported.bal.TOTAL_CURR_ASSETS == label ):
		Reported.ticker.TOTAL_CURR_ASSETS = row
		Reported.ticker.TOTAL_CURR_ASSETS[0] = label
	elif(Reported.bal.PPE_NET == label ):
		Reported.ticker.PPE_NET = row
		Reported.ticker.PPE_NET[0] = label
	elif(Reported.bal.PPE == label ):
		Reported.ticker.PPE = row
		Reported.ticker.PPE[0] = label
	elif(Reported.bal.ACC_DEPREC == label ):
		Reported.ticker.ACC_DEPREC = row
		Reported.ticker.ACC_DEPREC[0] = label
	elif(Reported.bal.LTI_RECEIVABLES == label ):
		Reported.ticker.LTI_RECEIVABLES = row
		Reported.ticker.LTI_RECEIVABLES[0] = label
	elif(Reported.bal.LT_INVEST == label ):
		Reported.ticker.LT_INVEST = row
		Reported.ticker.LT_INVEST[0] = label
	elif(Reported.bal.OTH_LT_ASSETS == label ):
		Reported.ticker.OTH_LT_ASSETS = row
		Reported.ticker.OTH_LT_ASSETS[0] = label
	elif(Reported.bal.TOTAL_INT_ASSETS == label ):
		Reported.ticker.TOTAL_INT_ASSETS = row
		Reported.ticker.TOTAL_INT_ASSETS[0] = label
	elif(Reported.bal.GOODWILL == label ):
		Reported.ticker.GOODWILL = row
		Reported.ticker.GOODWILL[0] = label
	elif(Reported.bal.OTH_INT_ASSETS == label ):
		Reported.ticker.OTH_INT_ASSETS = row
		Reported.ticker.OTH_INT_ASSETS[0] = label
	elif(Reported.bal.PREPAID_EXP == label ):
		Reported.ticker.PREPAID_EXP = row
		Reported.ticker.PREPAID_EXP[0] = label
	elif(Reported.bal.DEFF_TAX_ASSETS == label ):
		Reported.ticker.DEFF_TAX_ASSETS = row
		Reported.ticker.DEFF_TAX_ASSETS[0] = label
	elif(Reported.bal.DERIV_HEDGE_ASSETS2 == label ):
		Reported.ticker.DERIV_HEDGE_ASSETS2 = row
		Reported.ticker.DERIV_HEDGE_ASSETS2[0] = label
	elif(Reported.bal.MISC_ASSETS == label ):
		Reported.ticker.MISC_ASSETS = row
		Reported.ticker.MISC_ASSETS[0] = label
	elif(Reported.bal.TOTAL_NON_CURR_ASSETS == label ):
		Reported.ticker.TOTAL_NON_CURR_ASSETS = row
		Reported.ticker.TOTAL_NON_CURR_ASSETS[0] = label
	elif(Reported.bal.TOTAL_ASSETS2 == label ):
		Reported.ticker.TOTAL_ASSETS2 = row
		Reported.ticker.TOTAL_ASSETS2[0] = label
	elif(Reported.bal.LIAB_AND_EQUITY1 == label ):
		Reported.ticker.LIAB_AND_EQUITY1 = row
		Reported.ticker.LIAB_AND_EQUITY1[0] = label
	elif(Reported.bal.PAYABLES_ACCRUALS == label ):
		Reported.ticker.PAYABLES_ACCRUALS = row
		Reported.ticker.PAYABLES_ACCRUALS[0] = label
	elif(Reported.bal.PAYABLES == label ):
		Reported.ticker.PAYABLES = row
		Reported.ticker.PAYABLES[0] = label
	elif(Reported.bal.ACCRUED_TAXES == label ):
		Reported.ticker.ACCRUED_TAXES = row
		Reported.ticker.ACCRUED_TAXES[0] = label
	elif(Reported.bal.INT_DIVS_PAYABLES == label ):
		Reported.ticker.INT_DIVS_PAYABLES = row
		Reported.ticker.INT_DIVS_PAYABLES[0] = label
	elif(Reported.bal.OTH_PAYABLES_ACCURALS == label ):
		Reported.ticker.OTH_PAYABLES_ACCURALS = row
		Reported.ticker.OTH_PAYABLES_ACCURALS[0] = label
	elif(Reported.bal.ST_DEBT == label ):
		Reported.ticker.ST_DEBT = row
		Reported.ticker.ST_DEBT[0] = label
	elif(Reported.bal.ST_BORROWINGS == label ):
		Reported.ticker.ST_BORROWINGS = row
		Reported.ticker.ST_BORROWINGS[0] = label
	elif(Reported.bal.ST_FIN_LEASES == label ):
		Reported.ticker.ST_FIN_LEASES = row
		Reported.ticker.ST_FIN_LEASES[0] = label
	elif(Reported.bal.ST_OP_LEASES == label ):
		Reported.ticker.ST_OP_LEASES = row
		Reported.ticker.ST_OP_LEASES[0] = label
	elif(Reported.bal.CURR_LT_DEBT == label ):
		Reported.ticker.CURR_LT_DEBT = row
		Reported.ticker.CURR_LT_DEBT[0] = label
	elif(Reported.bal.OTH_ST_LIAB == label ):
		Reported.ticker.OTH_ST_LIAB = row
		Reported.ticker.OTH_ST_LIAB[0] = label
	elif(Reported.bal.DEFF_REV_1 == label ):
		Reported.ticker.DEFF_REV_1 = row
		Reported.ticker.DEFF_REV_1[0] = label
	elif(Reported.bal.DERIV_HEDGE_1 == label ):
		Reported.ticker.DERIV_HEDGE_1 = row
		Reported.ticker.DERIV_HEDGE_1[0] = label
	elif(Reported.bal.MISC_ST_LIAB == label ):
		Reported.ticker.MISC_ST_LIAB = row
		Reported.ticker.MISC_ST_LIAB[0] = label
	elif(Reported.bal.TOTAL_CURR_LIAB == label ):
		Reported.ticker.TOTAL_CURR_LIAB = row
		Reported.ticker.TOTAL_CURR_LIAB[0] = label
	elif(Reported.bal.LT_DEBT == label ):
		Reported.ticker.LT_DEBT = row
		Reported.ticker.LT_DEBT[0] = label
	elif(Reported.bal.LT_BORROW == label ):
		Reported.ticker.LT_BORROW = row
		Reported.ticker.LT_BORROW[0] = label
	elif(Reported.bal.LT_FIN_LEASES == label ):
		Reported.ticker.LT_FIN_LEASES = row
		Reported.ticker.LT_FIN_LEASES[0] = label
	elif(Reported.bal.LT_OP_LEASES == label ):
		Reported.ticker.LT_OP_LEASES = row
		Reported.ticker.LT_OP_LEASES[0] = label
	elif(Reported.bal.OTH_LT_LIAB == label ):
		Reported.ticker.OTH_LT_LIAB = row
		Reported.ticker.OTH_LT_LIAB[0] = label
	elif(Reported.bal.ACCURED_LIAB == label ):
		Reported.ticker.ACCURED_LIAB = row
		Reported.ticker.ACCURED_LIAB[0] = label
	elif(Reported.bal.PENSION_LIAB == label ):
		Reported.ticker.PENSION_LIAB = row
		Reported.ticker.PENSION_LIAB[0] = label
	elif(Reported.bal.OTH_POST_RET_BEN == label ):
		Reported.ticker.OTH_POST_RET_BEN = row
		Reported.ticker.OTH_POST_RET_BEN[0] = label
	elif(Reported.bal.PENSIONS == label ):
		Reported.ticker.PENSIONS = row
		Reported.ticker.PENSIONS[0] = label
	elif(Reported.bal.DEFF_REV_2 == label ):
		Reported.ticker.DEFF_REV_2 = row
		Reported.ticker.DEFF_REV_2[0] = label
	elif(Reported.bal.DEF_TAX_LIAB == label ):
		Reported.ticker.DEF_TAX_LIAB = row
		Reported.ticker.DEF_TAX_LIAB[0] = label
	elif(Reported.bal.DERIV_HEDGE_2 == label ):
		Reported.ticker.DERIV_HEDGE_2 = row
		Reported.ticker.DERIV_HEDGE_2[0] = label
	elif(Reported.bal.MISC_LT_LIAB == label ):
		Reported.ticker.MISC_LT_LIAB = row
		Reported.ticker.MISC_LT_LIAB[0] = label
	elif(Reported.bal.TOTAL_NON_CURR_LIAB == label ):
		Reported.ticker.TOTAL_NON_CURR_LIAB = row
		Reported.ticker.TOTAL_NON_CURR_LIAB[0] = label
	elif(Reported.bal.TOTAL_LIAB == label ):
		Reported.ticker.TOTAL_LIAB = row
		Reported.ticker.TOTAL_LIAB[0] = label
	elif(Reported.bal.PREF_EQUITY_HYBRID_CAP == label ):
		Reported.ticker.PREF_EQUITY_HYBRID_CAP = row
		Reported.ticker.PREF_EQUITY_HYBRID_CAP[0] = label
	elif(Reported.bal.SHARE_CAP_APIC == label ):
		Reported.ticker.SHARE_CAP_APIC = row
		Reported.ticker.SHARE_CAP_APIC[0] = label
	elif(Reported.bal.COMMON_STOCK == label ):
		Reported.ticker.COMMON_STOCK = row
		Reported.ticker.COMMON_STOCK[0] = label
	elif(Reported.bal.ADD_PAID_CAP == label ):
		Reported.ticker.ADD_PAID_CAP = row
		Reported.ticker.ADD_PAID_CAP[0] = label
	elif(Reported.bal.TREASURY_STOCK == label ):
		Reported.ticker.TREASURY_STOCK = row
		Reported.ticker.TREASURY_STOCK[0] = label
	elif(Reported.bal.RE == label ):
		Reported.ticker.RE = row
		Reported.ticker.RE[0] = label
	elif(Reported.bal.OTH_EQUITY == label ):
		Reported.ticker.OTH_EQUITY = row
		Reported.ticker.OTH_EQUITY[0] = label
	elif(Reported.bal.EQUITY_BEFORE_MIN_INT == label ):
		Reported.ticker.EQUITY_BEFORE_MIN_INT = row
		Reported.ticker.EQUITY_BEFORE_MIN_INT[0] = label
	elif(Reported.bal.MIN_NON_CONTROL_INT == label ):
		Reported.ticker.MIN_NON_CONTROL_INT = row
		Reported.ticker.MIN_NON_CONTROL_INT[0] = label
	elif(Reported.bal.TOTAL_EQUITY == label ):
		Reported.ticker.TOTAL_EQUITY = row
		Reported.ticker.TOTAL_EQUITY[0] = label
	elif(Reported.bal.LIAB_AND_EQUITY2 == label ):
		Reported.ticker.LIAB_AND_EQUITY2 = row
		Reported.ticker.LIAB_AND_EQUITY2[0] = label
	else:
		unkept.append(label)

print("\n\n******************************")
print("CF")
print("******************************")
for index, row in cf.iterrows():
	if(Reported.cf.NI_CF == label ):
		Reported.ticker.NI_CF = row
		Reported.ticker.NI_CF[0] = label
	elif(Reported.cf.DEPRE_AMORT == label ):
		Reported.ticker.DEPRE_AMORT = row
		Reported.ticker.DEPRE_AMORT[0] = label
	elif(Reported.cf.NON_CASH_ITEMS == label ):
		Reported.ticker.NON_CASH_ITEMS = row
		Reported.ticker.NON_CASH_ITEMS[0] = label
	elif(Reported.cf.STOCK_COMP == label ):
		Reported.ticker.STOCK_COMP = row
		Reported.ticker.STOCK_COMP[0] = label
	elif(Reported.cf.DEF_INT_COMP == label ):
		Reported.ticker.DEF_INT_COMP = row
		Reported.ticker.DEF_INT_COMP[0] = label
	elif(Reported.cf.OTH_NON_CASH_ADJ == label ):
		Reported.ticker.OTH_NON_CASH_ADJ = row
		Reported.ticker.OTH_NON_CASH_ADJ[0] = label
	elif(Reported.cf.CHG_NON_CASH_OP == label ):
		Reported.ticker.CHG_NON_CASH_OP = row
		Reported.ticker.CHG_NON_CASH_OP[0] = label
	elif(Reported.cf.CHG_ACCTS_REC == label ):
		Reported.ticker.CHG_ACCTS_REC = row
		Reported.ticker.CHG_ACCTS_REC[0] = label
	elif(Reported.cf.CHG_INVENTORIES == label ):
		Reported.ticker.CHG_INVENTORIES = row
		Reported.ticker.CHG_INVENTORIES[0] = label
	elif(Reported.cf.CHG_ACCTS_PAYABLE == label ):
		Reported.ticker.CHG_ACCTS_PAYABLE = row
		Reported.ticker.CHG_ACCTS_PAYABLE[0] = label
	elif(Reported.cf.CHG_OTHER == label ):
		Reported.ticker.CHG_OTHER = row
		Reported.ticker.CHG_OTHER[0] = label
	elif(Reported.cf.NET_CASH_DISC_OPS1 == label ):
		Reported.ticker.NET_CASH_DISC_OPS1 = row
		Reported.ticker.NET_CASH_DISC_OPS1[0] = label
	elif(Reported.cf.CASH_OP_ACT == label ):
		Reported.ticker.CASH_OP_ACT = row
		Reported.ticker.CASH_OP_ACT[0] = label
	elif(Reported.cf.CASH_INVEST_ACT1 == label ):
		Reported.ticker.CASH_INVEST_ACT1 = row
		Reported.ticker.CASH_INVEST_ACT1[0] = label
	elif(Reported.cf.CHG_FIXED_INTANG == label ):
		Reported.ticker.CHG_FIXED_INTANG = row
		Reported.ticker.CHG_FIXED_INTANG[0] = label
	elif(Reported.cf.DISP_FIXED_INTANG == label ):
		Reported.ticker.DISP_FIXED_INTANG = row
		Reported.ticker.DISP_FIXED_INTANG[0] = label
	elif(Reported.cf.DISP_FIXED_PROD_ASSETS == label ):
		Reported.ticker.DISP_FIXED_PROD_ASSETS = row
		Reported.ticker.DISP_FIXED_PROD_ASSETS[0] = label
	elif(Reported.cf.DISP_INTAG_ASSETS == label ):
		Reported.ticker.DISP_INTAG_ASSETS = row
		Reported.ticker.DISP_INTAG_ASSETS[0] = label
	elif(Reported.cf.ACQ_FIXED_INTAG == label ):
		Reported.ticker.ACQ_FIXED_INTAG = row
		Reported.ticker.ACQ_FIXED_INTAG[0] = label
	elif(Reported.cf.ACQ_FIXED_PROD_ASSETS == label ):
		Reported.ticker.ACQ_FIXED_PROD_ASSETS = row
		Reported.ticker.ACQ_FIXED_PROD_ASSETS[0] = label
	elif(Reported.cf.ACQ_INTAG_ASSETS == label ):
		Reported.ticker.ACQ_INTAG_ASSETS = row
		Reported.ticker.ACQ_INTAG_ASSETS[0] = label
	elif(Reported.cf.NET_CHG_LT_INVEST == label ):
		Reported.ticker.NET_CHG_LT_INVEST = row
		Reported.ticker.NET_CHG_LT_INVEST[0] = label
	elif(Reported.cf.DEC_LT_INVEST == label ):
		Reported.ticker.DEC_LT_INVEST = row
		Reported.ticker.DEC_LT_INVEST[0] = label
	elif(Reported.cf.INC_LT_INVEST == label ):
		Reported.ticker.INC_LT_INVEST = row
		Reported.ticker.INC_LT_INVEST[0] = label
	elif(Reported.cf.NET_CASH_ACQ_DIV == label ):
		Reported.ticker.NET_CASH_ACQ_DIV = row
		Reported.ticker.NET_CASH_ACQ_DIV[0] = label
	elif(Reported.cf.CASH_DIVEST == label ):
		Reported.ticker.CASH_DIVEST = row
		Reported.ticker.CASH_DIVEST[0] = label
	elif(Reported.cf.CASH_ACQ_SUBS == label ):
		Reported.ticker.CASH_ACQ_SUBS = row
		Reported.ticker.CASH_ACQ_SUBS[0] = label
	elif(Reported.cf.CASH_JVS == label ):
		Reported.ticker.CASH_JVS = row
		Reported.ticker.CASH_JVS[0] = label
	elif(Reported.cf.OTH_INVEST_ACT == label ):
		Reported.ticker.OTH_INVEST_ACT = row
		Reported.ticker.OTH_INVEST_ACT[0] = label
	elif(Reported.cf.NET_CASH_DISC_OPS2 == label ):
		Reported.ticker.NET_CASH_DISC_OPS2 = row
		Reported.ticker.NET_CASH_DISC_OPS2[0] = label
	elif(Reported.cf.CASH_INVEST_ACT2 == label ):
		Reported.ticker.CASH_INVEST_ACT2 = row
		Reported.ticker.CASH_INVEST_ACT2[0] = label
	elif(Reported.cf.CASH_FIN_ACT2 == label ):
		Reported.ticker.CASH_FIN_ACT2 = row
		Reported.ticker.CASH_FIN_ACT2[0] = label
	elif(Reported.cf.DIVS_PAID == label ):
		Reported.ticker.DIVS_PAID = row
		Reported.ticker.DIVS_PAID[0] = label
	elif(Reported.cf.CASH_REPAY_DEBT == label ):
		Reported.ticker.CASH_REPAY_DEBT = row
		Reported.ticker.CASH_REPAY_DEBT[0] = label
	elif(Reported.cf.CASH_ST_DEBT == label ):
		Reported.ticker.CASH_ST_DEBT = row
		Reported.ticker.CASH_ST_DEBT[0] = label
	elif(Reported.cf.CASH_LT_DEBT == label ):
		Reported.ticker.CASH_LT_DEBT = row
		Reported.ticker.CASH_LT_DEBT[0] = label
	elif(Reported.cf.REPAY_LT_DEBT == label ):
		Reported.ticker.REPAY_LT_DEBT = row
		Reported.ticker.REPAY_LT_DEBT[0] = label
	elif(Reported.cf.CASH_REPURCH_EQUITY == label ):
		Reported.ticker.CASH_REPURCH_EQUITY = row
		Reported.ticker.CASH_REPURCH_EQUITY[0] = label
	elif(Reported.cf.INC_CAPITAL_STOCK == label ):
		Reported.ticker.INC_CAPITAL_STOCK = row
		Reported.ticker.INC_CAPITAL_STOCK[0] = label
	elif(Reported.cf.DEC_CAPITAL_STOCK == label ):
		Reported.ticker.DEC_CAPITAL_STOCK = row
		Reported.ticker.DEC_CAPITAL_STOCK[0] = label
	elif(Reported.cf.OTH_FIN_ACT == label ):
		Reported.ticker.OTH_FIN_ACT = row
		Reported.ticker.OTH_FIN_ACT[0] = label
	elif(Reported.cf.NET_CASH_DISC_OPS3 == label ):
		Reported.ticker.NET_CASH_DISC_OPS3 = row
		Reported.ticker.NET_CASH_DISC_OPS3[0] = label
	elif(Reported.cf.CASH_FIN_ACT2 == label ):
		Reported.ticker.CASH_FIN_ACT2 = row
		Reported.ticker.CASH_FIN_ACT2[0] = label
	elif(Reported.cf.EFFECT_FOREX_RATES == label ):
		Reported.ticker.EFFECT_FOREX_RATES = row
		Reported.ticker.EFFECT_FOREX_RATES[0] = label
	elif(Reported.cf.NET_CHG_CASH == label ):
		Reported.ticker.NET_CHG_CASH = row
		Reported.ticker.NET_CHG_CASH[0] = label
	elif(Reported.cf.CASH_PAID_TAXES == label ):
		Reported.ticker.CASH_PAID_TAXES = row
		Reported.ticker.CASH_PAID_TAXES[0] = label
	elif(Reported.cf.CASH_PAID_INT == label ):
		Reported.ticker.CASH_PAID_INT = row
		Reported.ticker.CASH_PAID_INT[0] = label
	else:
		unkept.append(label)

