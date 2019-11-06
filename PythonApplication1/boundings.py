import Enums
import instantiate


def genRatings(data, dataCalcs):
	
	ratings = instantiate.instantiateDataCalc(data)
	#dataCalcs['symbol'] = data['symbol']

	#dataCalcs['YEAR_INC']
	#dataCalcs['YEAR_BAL']
	#dataCalcs['YEAR_CF'] 
	#dataCalcs['MARGINAL_TAX_RATE']
	#dataCalcs['FAIR_RETURN_RATE'] 
	#dataCalcs['NO_GROWTH_PE'] 
	#dataCalcs['REQUIRED_RETURN'] 
	#dataCalcs['AAA_BOND_YIELD'] 
	#dataCalcs['GROWTH_MULTIPLE']
	#dataCalcs['REV_GROWTH_RATE']
	#dataCalcs['EBITDA_GROWTH_RATE']
	#dataCalcs['EBIT_GROWTH_RATE']
	#dataCalcs['NI_GROWTH_RATE']
	#dataCalcs['EPS_GROWTH_RATE']
	#dataCalcs['GROWTH_RATE']
	#dataCalcs['AVG_3YEARS'] 
	#dataCalcs['AVG_5YEARS'] 
	#dataCalcs['COST_OF_SALES']
	#dataCalcs['WORKING_CAPITAL']
	#dataCalcs['CAPITAL_EMPLOYED']
	#dataCalcs['TOTAL_INVEST']
	#dataCalcs['TOTAL_DEBT']
	#dataCalcs['EBITDA']
	#dataCalcs['EBIAT']
	#dataCalcs['EBIT'] 
	#dataCalcs['CAPEX']
	#dataCalcs['LEV_FCF']
	#dataCalcs['UN_LEV_FCF']
	#dataCalcs['AVG_RECEIVABLES']
	#dataCalcs['AVG_PAYABLES_ACCRUALS']
	#dataCalcs['AVG_WORKING_CAPITAL']
	#dataCalcs['AVG_INVENTORY']
	#dataCalcs['AVG_INVEST'] 
	#dataCalcs['AVG_LT_ASSETS']
	#dataCalcs['AVG_ASSETS']
	#dataCalcs['AVG_LIABILITIES']
	#dataCalcs['AVG_EQUITY']
	#dataCalcs['AVG_DEBT'] 
	
	i = 1
	# Dependent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalcs['YEAR_INC'][i] != dataCalcs['YEAR_BAL'][i] and dataCalcs['YEAR_CF'][i] != dataCalcs['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalcs['YEAR_INC'][i], dataCalcs['YEAR_BAL'][i], dataCalcs['YEAR_CF'][i])
			break
		ratings['CASH_RATIO'][i] = rateCashRatio(dataCalcs['CASH_RATIO'][i])
		ratings['CASH_STI_RATIO'][i] = rateCashRatio(dataCalcs['CASH_STI_RATIO'][i])
		ratings['CASH_SERVICE_RATIO'][i] = rateCashServiceRatio(dataCalcs['CASH_SERVICE_RATIO'][i])
		ratings['INT_SERVICE_RATIO'][i] = rateInterestServiceRatio(dataCalcs['INT_SERVICE_RATIO'][i])
		ratings['CASH_ST_DEBT_RATIO'][i] = rateCashRatio(dataCalcs['CASH_ST_DEBT_RATIO'][i])
		ratings['ACID_TEST'][i] = rateAcidTestRatio(dataCalcs['ACID_TEST'][i])
		ratings['QUICK_RATIO'][i] = rateQuickRatio(dataCalcs['QUICK_RATIO'][i])
		ratings['QUICK_RATIO_2'][i] = rateQuick2Ratio(dataCalcs['QUICK_RATIO_2'][i])
		ratings['CURRENT_RATIO'][i] = rateCurrentRatio(dataCalcs['CURRENT_RATIO'][i])
		ratings['WORKING_CAP_RATIO'][i] = rateWorkingCapRatio(dataCalcs['WORKING_CAP_RATIO'][i])
		ratings['DEBT_SERVICE_RATIO'][i] = rateDebtServiceRatio(dataCalcs['DEBT_SERVICE_RATIO'][i])
		#ratings[''][i] = 
	#dataCalcs['NET_DEBT']
	#dataCalcs['DEBT_RATIO']
	#dataCalcs['DEBT_EQ_RATIO']
	#dataCalcs['DEBT_TO_NI']
	#dataCalcs['FIXED_CHARGE_COVERAGE']
	#dataCalcs['DEGREE_COMBINED_LEV']
	#dataCalcs['DEGREE_OPERATING_LEV']
	#dataCalcs['DEGREE_FINANCIAL_LEV']
	#dataCalcs['DFL_RATIO'] 
	#dataCalcs['FINANCIAL_LEVERAGE']
	#dataCalcs['EQUITY_RATIO']
	#dataCalcs['EQUITY_MULTIPLIER_RATIO_1']
	#dataCalcs['EQUITY_MULTIPLIER_RATIO_2']
	#dataCalcs['NAV'] 
	#dataCalcs['EFFECTIVE_INT_RATE'] 
	#dataCalcs['DEBT_COST_CAP']
	#dataCalcs['WACC']
	#dataCalcs['SALES_TURNOVER'] 
	#dataCalcs['DSO'] 
	#dataCalcs['ASSET_TURNOVER'] 
	#dataCalcs['ASSET_TURN_RATE']
	#dataCalcs['LT_ASSET_TURNOVER']
	#dataCalcs['LT_ASSET_TURN_RATE']
	#dataCalcs['INV_SALES_TURNOVER'] 
	#dataCalcs['DSI'] 
	#dataCalcs['INV_COGS_TURNOVER'] 
	#dataCalcs['DIO'] 
	#dataCalcs['RECEIVABLES_ACCTS_TURNOVER'] 
	#dataCalcs['DRO'] 
	#dataCalcs['WORKING_CAP_TURNOVER'] 
	#dataCalcs['DWC'] 
	#dataCalcs['ROI_INVESTMENTS'] 
	#dataCalcs['CREDITORS_TURNOVER'] 
	#dataCalcs['CDO'] 
	#dataCalcs['PAYABLES_TURNOVER_COGS'] 
	#dataCalcs['DPO_COGS'] 
	#dataCalcs['PAYABLES_TURNOVER_COS'] 
	#dataCalcs['DPO_COS'] 
	#dataCalcs['LIAB_TURNOVER'] 
	#dataCalcs['LIAB_TURN_RATE'] 
	#dataCalcs['CHG_DEBT_REPAYMENT_REQ'] 
	#dataCalcs['DEBTORS_PAYBACK_PERIOD'] 
	#dataCalcs['BURN_RATE'] 
	#dataCalcs['CCC'] 
	#dataCalcs['ROS'] 
	#dataCalcs['ROE'] 
	#dataCalcs['ROA'] 
	#dataCalcs['ROCE_NI']
	#dataCalcs['EPS_DILUTED_NI']
	#dataCalcs['EPS_DILUTED_EBIT']
	#dataCalcs['ROCE_EBIT'] 
	#dataCalcs['PE'] 
	#dataCalcs['PE_REL_3'] 
	#dataCalcs['PE_REL_5'] 
	#dataCalcs['EARNINGS_POWER']
	#dataCalcs['GROSS_MARGIN']
	#dataCalcs['NOPAT_NI']
	#dataCalcs['NOPAT_EBIT']
	#dataCalcs['ROIC'] 
	#dataCalcs['OPERATING_RATIO'] 
	#dataCalcs['OP_PROFIT_MARGIN']
	#dataCalcs['MV'] 
	#dataCalcs['MV_EBIT_RATIO'] 
	#dataCalcs['ORIG_GRAHAM']
	#dataCalcs['REVISED_GRAHAM']
	#dataCalcs['EV'] 
	#dataCalcs['EV_EBIT'] 
	#dataCalcs['EV_NI']
	#dataCalcs['BV'] 
	#dataCalcs['BV_PER_SHARE'] 
	#dataCalcs['BV_NI']
	#dataCalcs['BV_EBIT']
	#dataCalcs['PRICE_SALES']
	#dataCalcs['PRICE_BOOK'] 
	#dataCalcs['PRICE_NAV'] 
	#dataCalcs['PRICE_FCF'] 
	#dataCalcs['PRICE_UN_FCF']
	#dataCalcs['MV_OCF'] 
	#dataCalcs['CASH_PRICE_RATIO'] 
	#dataCalcs['INTRINSIC_VALUE_NI']
	#dataCalcs['INTRINSIC_VALUE_EBIT']
	#dataCalcs['INTRINSIC_VALUE_FCF'] 
	#dataCalcs['MARGIN_OF_QUESTIONABLETY_NI'] 
	#dataCalcs['MARGIN_OF_QUESTIONABLETY_EBIT']
	#dataCalcs['MARGIN_OF_QUESTIONABLETY_FCF'] 
	#dataCalcs['DUPONT_SYSTEM_1'] 
	#dataCalcs['DUPONT_SYSTEM_2'] 
	#dataCalcs['RETENTION_RATIO'] 
	#dataCalcs['DIV_PAYOUT_RATIO']
	#dataCalcs['EARNINGS_YIELD'] 
	#dataCalcs['DIVS_YIELD'] 
	#dataCalcs['SGR'] 
		i += 1
	print(ratings['CASH_ST_DEBT_RATIO'])
	return ratings
	

def rateCashRatio(CASH_RATIO):

	if(CASH_RATIO == None):
		return None

	if(CASH_RATIO < 0.5):
		return Enums.Rating.AT_RISK
	elif(1 < CASH_RATIO):
		return Enums.Rating.HEALTHY
	else:
		return Enums.Rating.QUESTIONABLE

	
def rateCashServiceRatio(CASH_SERVICE_RATIO):

	if(CASH_SERVICE_RATIO == None):
		return None

	if(CASH_SERVICE_RATIO < 1):
		return Enums.Rating.AT_RISK
	elif(1.5 < CASH_SERVICE_RATIO):
		return Enums.Rating.HEALTHY
	else:
		return Enums.Rating.QUESTIONABLE

		
def rateInterestServiceRatio(INT_SERVICE_RATIO):

	if(INT_SERVICE_RATIO == None):
		return None

	if(INT_SERVICE_RATIO < 1):
		return Enums.Rating.AT_RISK
	elif(1.5 < INT_SERVICE_RATIO):
		return Enums.Rating.HEALTHY
	else:
		return Enums.Rating.QUESTIONABLE

#def rateAcidTestRatio(ACID_TEST):
#def rateQuickRatio(QUICK_RATIO_2):
#def rateQuickRatio2(QUICK_RATIO_2):
#def rateCurrentRatio(CURRENT_RATIO):
#def rateWorkingCapRatio(WORKING_CAP_RATIO):
#def rateDebtServiceRatio(DEBT_SERVICE_RATIO):
#def ():
#def ():