import Enums
import instantiate
import Calcs
import json
import inspect
import numpy as np


def getTickerObject():
	omit = "as_integer_ratio", "conjugate", "fromhex", "hex", "imag", "is_integer", "real"
	return [x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ]

def ToFile(path, fileName, data):
	filePathNameExt = './' + path + '/' + fileName + 'Rating' + '.json'
	
	with open(filePathNameExt, 'w') as fp:
		json.dump(data, fp)


def decorateFile(path, fileName):
	myfile = open(fileName, "r+")
	contents = myfile.read()        
	contents = contents.replace('nan', 'null').replace('None', 'null').replace('\"\\\"[', '[').replace(']\\\"\"', ']')
	contents = contents.replace('\"[', '[').replace(']\"', ']').replace('\\\"', '\'').replace('Shareholders\'', 'Shareholders')
	contents = contents.replace('\'', '\"')
	newFile = open(fileName, "w")
	newFile.write(contents)        
	myfile.close()               
	newFile.close()  

path = './'


def genRatings(dataFile, dataCalcFile):
	
	with open(dataFile) as json_file:
		data = json.load(json_file)
	with open(dataCalcFile) as json_file:
		dataCalc = json.load(json_file)

	upperThird = 66.66
	lowerThird = 33.33
	mid = 50

	ratings = instantiate.instantiateDataCalc()
	ratings['SECTOR'] = "Sector name goes here"
	ratings['DECISION'] = [0] * 35
	ratings['DECISION'] = [None] * 35
	ratings['DECISION'][0] = "Evaluation Decision"

	#dataCalc['symbol'] = data['symbol']

	#dataCalc['YEAR_INC']
	#dataCalc['YEAR_BAL']
	#dataCalc['YEAR_CF'] 
	#dataCalc['MARGINAL_TAX_RATE']
	#dataCalc['FAIR_RETURN_RATE'] 
	#dataCalc['NO_GROWTH_PE'] 
	#dataCalc['REQUIRED_RETURN'] 
	#dataCalc['AAA_BOND_YIELD'] 
	#dataCalc['GROWTH_MULTIPLE']
	#dataCalc['REV_GROWTH_RATE']
	#dataCalc['EBITDA_GROWTH_RATE']
	#dataCalc['EBIT_GROWTH_RATE']
	#dataCalc['NI_GROWTH_RATE']
	#dataCalc['EPS_GROWTH_RATE']
	#dataCalc['GROWTH_RATE']
	#dataCalc['AVG_3YEARS'] 
	#dataCalc['AVG_5YEARS'] 
	#dataCalc['COST_OF_SALES']
	#dataCalc['WORKING_CAPITAL']
	#dataCalc['CAPITAL_EMPLOYED']
	#dataCalc['TOTAL_INVEST']
	#dataCalc['TOTAL_DEBT']
	#dataCalc['EBITDA']
	#dataCalc['EBIAT']
	#dataCalc['EBIT'] 
	#dataCalc['CAPEX']
	#dataCalc['LEV_FCF']
	#dataCalc['UN_LEV_FCF']
	#dataCalc['AVG_RECEIVABLES']
	#dataCalc['AVG_PAYABLES_ACCRUALS']
	#dataCalc['AVG_WORKING_CAPITAL']
	#dataCalc['AVG_INVENTORY']
	#dataCalc['AVG_INVEST'] 
	#dataCalc['AVG_LT_ASSETS']
	#dataCalc['AVG_ASSETS']
	#dataCalc['AVG_LIABILITIES']
	#dataCalc['AVG_EQUITY']
	#dataCalc['AVG_DEBT'] 
	
	i = 1
	# Dependent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break
		ratings['CASH_RATIO'][i] = halfToOne(dataCalc['CASH_RATIO'][i])
		ratings['CASH_STI_RATIO'][i] = halfToOne(dataCalc['CASH_STI_RATIO'][i])
		ratings['CASH_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['CASH_SERVICE_RATIO'][i])
		ratings['INT_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['INT_SERVICE_RATIO'][i])
		ratings['CASH_ST_DEBT_RATIO'][i] = halfToOne(dataCalc['CASH_ST_DEBT_RATIO'][i])
		ratings['ACID_TEST'][i] = onetoOneAndHalf(dataCalc['ACID_TEST'][i])
		ratings['QUICK_RATIO'][i] = onetoOneAndHalf(dataCalc['QUICK_RATIO'][i])
		ratings['QUICK_RATIO_2'][i] = onetoOneAndHalf(dataCalc['QUICK_RATIO_2'][i])
		ratings['CURRENT_RATIO'][i] = onetoOneAndHalf(dataCalc['CURRENT_RATIO'][i])
		#ratings['NWC_TO_TA'][i] = unknown() #Compare against sector
		ratings['DEBT_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['DEBT_SERVICE_RATIO'][i])
		#ratings['NET_DEBT'][i] = unknown() #Compare against sector
		ratings['DEBT_RATIO'][i] = rateDebtRisk(dataCalc['DEBT_RATIO'][i])
		#Determine an appropriate industry average of debt to base relative debt load against
		#ratings['DEBT_EQ_RATIO'][i] = sectorRankDown(['DEBT_EQ_RATIO'][i], np.percentile(industry['DEBT_EQ_RATIO'][i], lowerThird), np.percentile(industry['DEBT_EQ_RATIO'][i], upperThird) )
		#ratings['ST_DEBT_EQ_RATIO'][i] = stLtDebtRisk(dataCalc['DEBT_EQ_RATIO'][i], data['ST_DEBT_RATIO'][i], industry['DEBT_EQ_RATIO'][i], industry['ST_DEBT_RATIO_25'][i], industry['ST_DEBT_RATIO_75'][i])
		#ratings['LT_DEBT_EQ_RATIO'][i] = stLtDebtRisk(dataCalc['DEBT_EQ_RATIO'][i], data['LT_DEBT_RATIO'][i], industry['DEBT_EQ_RATIO'][i], industry['LT_DEBT_RATIO_25'][i], industry['LT_DEBT_RATIO_75'][i])
		
		ratings['DEBT_TO_EBIT'][i] = rateDebtEbitRatio(dataCalc['DEBT_TO_EBIT'][i])
		ratings['FIXED_CHARGE_COVERAGE'][i] = rateFCCR(dataCalc['FIXED_CHARGE_COVERAGE'][i])
		#ratings['DEGREE_COMBINED_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_COMBINED_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_COMBINED_LEV_50'][i])
		#ratings['DEGREE_OPERATING_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_OPERATING_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_COMBINED_LEV_50'][i])
		#ratings['DEGREE_FINANCIAL_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_FINANCIAL_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_COMBINED_LEV_50'][i])
		#ratings['DFL_RATIO'][i] = rateDegreeOfLeverage(dataCalc['DFL_RATIO'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_COMBINED_LEV_50'][i])

		ratings['FINANCIAL_LEVERAGE'][i] = rateFL(dataCalc['FINANCIAL_LEVERAGE'][i])
		#ratings['EQUITY_RATIO'][i] = sectorRankUp(dataCalc['EQUITY_RATIO'][i], np.percentile(industry['EQUITY_RATIO'][i], lowerThird), np.percentile(industry['EQUITY_RATIO'][i], upperThird) )
		#ratings['EQUITY_MULTIPLIER_RATIO_1'][i] = rateEqMult1(dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i], industry['EQUITY_MULTIPLIER_RATIO_1_25'][i], industry['EQUITY_MULTIPLIER_RATIO_1_75'][i])
		
		ratings['EQUITY_MULTIPLIER_RATIO_2'][i] = rateDebtRisk(dataCalc['DEBT_RATIO'][i]) #Note: equations are same math
		#ratings['NAV'][i] = unknown() #Compare against sector
		ratings['EFFECTIVE_INT_RATE'][i] = rateCostOfDebt(dataCalc['EFFECTIVE_INT_RATE'][i], dataCalc['ROCE_EBIT'][i])
		ratings['DEBT_COST_CAP'][i] = rateCostOfDebt(dataCalc['DEBT_COST_CAP'][i], dataCalc['ROCE_NI'][i])
		#ratings['WACC'][i] = sectorRankDown(dataCalc['WACC'][i], np.percentile(industry['WACC'][i], lowerThird), np.percentile(industry['WACC'][i], upperThird) )
		#ratings['SALES_TURNOVER'][i] = sectorRankUp(dataCalc['SALES_TURNOVER'][i], np.percentile(industry['SALES_TURNOVER'][i], lowerThird), np.percentile(industry['SALES_TURNOVER'][i], upperThird) )
		#ratings['DSO'][i] = sectorRankDown(dataCalc['DSO'][i], np.percentile(industry['DSO'][i], lowerThird), np.percentile(industry['DSO'][i], upperThird) )
		#ratings['ASSET_TURNOVER'][i] = sectorRankUp(dataCalc['ASSET_TURNOVER'][i], np.percentile(industry['ASSET_TURNOVER'][i], lowerThird), np.percentile(industry['ASSET_TURNOVER'][i], upperThird) )
		#ratings['ASSET_TURN_RATE'][i] = sectorRankUp(dataCalc['ASSET_TURN_RATE'][i], np.percentile(industry['ASSET_TURN_RATE'][i], lowerThird), np.percentile(industry['ASSET_TURN_RATE'][i], upperThird) )
		#ratings['LT_ASSET_TURNOVER'][i] = sectorRankUp(dataCalc['LT_ASSET_TURNOVER'][i], np.percentile(industry['LT_ASSET_TURNOVER'][i], lowerThird), np.percentile(industry['LT_ASSET_TURNOVER'][i], upperThird) )
		#ratings['LT_ASSET_TURN_RATE'][i] = sectorRankUp(dataCalc['LT_ASSET_TURN_RATE'][i], np.percentile(industry['LT_ASSET_TURN_RATE'][i], lowerThird), np.percentile(industry['LT_ASSET_TURN_RATE'][i], upperThird) )
		#ratings['INV_SALES_TURNOVER'][i] = sectorRankUp(dataCalc['INV_SALES_TURNOVER'][i], np.percentile(industry['INV_SALES_TURNOVER'][i], lowerThird), np.percentile(industry['INV_SALES_TURNOVER'][i], upperThird) )
		#ratings['DSI'][i] = sectorRankUp(dataCalc['DSI'][i], np.percentile(industry['DSI'][i], lowerThird), np.percentile(industry['DSI'][i], upperThird) )
		#ratings['INV_COGS_TURNOVER'][i] = dataCalc['INV_COGS_TURNOVER'][i] 
		#ratings['DIO'][i] = dataCalc['DIO'][i] 
		#ratings['RECEIVABLES_ACCTS_TURNOVER'][i] = dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i] 
		#ratings['DRO'][i] = dataCalc['DRO'][i] 
		#ratings['WORKING_CAP_TURNOVER'][i] = dataCalc['WORKING_CAP_TURNOVER'][i] 
		#ratings['DWC'][i] = dataCalc[DWC'DWC'][i] 
		#ratings['ROI_INVESTMENTS'][i] = dataCalc['ROI_INVESTMENTS'][i] 
		#ratings['CREDITORS_TURNOVER'][i] = dataCalc['CREDITORS_TURNOVER'][i] 
		#ratings['CDO'][i] = dataCalc['CDO'][i] 
		#ratings['PAYABLES_TURNOVER_COGS'][i] = dataCalc['PAYABLES_TURNOVER_COGS'][i] 
		#ratings['DPO_COGS'][i] = dataCalc['DPO_COGS'][i] 
		#ratings['PAYABLES_TURNOVER_COS'][i] = dataCalc['PAYABLES_TURNOVER_COS'][i] 
		#ratings['DPO_COS'][i] = dataCalc['DPO_COS'][i] 
		#ratings['LIAB_TURNOVER'][i] = dataCalc['LIAB_TURNOVER'][i] 
		#ratings['LIAB_TURN_RATE'][i] = dataCalc['LIAB_TURN_RATE'][i] 
		#ratings['CHG_DEBT_REPAYMENT_REQ'][i] = dataCalc['CHG_DEBT_REPAYMENT_REQ'][i] 
		#ratings['DEBTORS_PAYBACK_PERIOD'][i] = dataCalc['DEBTORS_PAYBACK_PERIOD'][i] 
		#ratings['BURN_RATE'][i] = dataCalc['BURN_RATE'][i] 
		#ratings['CCC'][i] = dataCalc['CCC'][i] 
		#ratings['ROS'][i] = dataCalc['ROS'][i] 
		#ratings['ROE'][i] = dataCalc['ROE'][i] 
		#ratings['ROA'][i] = dataCalc['ROA'][i] 
		#ratings['ROCE_NI'][i] = dataCalc['ROCE_NI'][i]
		#ratings['EPS_DILUTED_NI'][i] = dataCalc['EPS_DILUTED_NI'][i]
		#ratings['EPS_DILUTED_EBIT'][i] = dataCalc['EPS_DILUTED_EBIT'][i]
		#ratings['ROCE_EBIT'][i] = dataCalc['ROCE_EBIT'][i] 
		#ratings['PE'][i] = dataCalc['PE'][i] 
		#ratings['PE_REL_3'][i] = dataCalc['PE_REL_3'][i] 
		#ratings['PE_REL_5'][i] = dataCalc['PE_REL_5'][i] 
		#ratings['EARNINGS_POWER'][i] = dataCalc['EARNINGS_POWER'][i]
		#ratings['GROSS_MARGIN'][i] = dataCalc['GROSS_MARGIN'][i]
		#ratings['NOPAT_NI'][i] = dataCalc['NOPAT_NI'][i]
		#ratings['NOPAT_EBIT'][i] = dataCalc['NOPAT_EBIT'][i]
		#ratings['ROIC'][i] = dataCalc['ROIC'][i] 
		#ratings['OPERATING_RATIO'][i] = dataCalc['OPERATING_RATIO'][i] 
		#ratings['OP_PROFIT_MARGIN'][i] = dataCalc['OP_PROFIT_MARGIN'][i]
		#ratings['MV'][i] = dataCalc['MV'][i] 
		#ratings['MV_EBIT_RATIO'][i] = dataCalc['MV_EBIT_RATIO'][i] 
		#ratings['ORIG_GRAHAM'][i] = dataCalc['ORIG_GRAHAM'][i]
		#ratings['REVISED_GRAHAM'][i] = dataCalc['REVISED_GRAHAM'][i]
		#ratings['EV'][i] = dataCalc['EV'][i] 
		#ratings['EV_EBIT'][i] = dataCalc['EV_EBIT'][i] 
		#ratings['EV_NI'][i] = dataCalc['EV_NI'][i]
		#ratings['BV'][i] = dataCalc['BV'][i] 
		#ratings['BV_PER_SHARE'][i] = dataCalc['BV_PER_SHARE'][i] 
		#ratings['BV_NI'][i] = dataCalc['BV_NI'][i]
		#ratings['BV_EBIT'][i] = dataCalc['BV_EBIT'][i]
		#ratings['PRICE_SALES'][i] = dataCalc['PRICE_SALES'][i]
		#ratings['PRICE_BOOK'][i] = dataCalc['PRICE_BOOK'][i] 
		#ratings['PRICE_NAV'][i] = dataCalc['PRICE_NAV'][i] 
		#ratings['PRICE_FCF'][i] = dataCalc['PRICE_FCF'][i] 
		#ratings['PRICE_UN_FCF'][i] = dataCalc['PRICE_UN_FCF'][i]
		#ratings['MV_OCF'][i] = dataCalc['MV_OCF'][i] 
		#ratings['CASH_PRICE_RATIO'][i] = dataCalc['CASH_PRICE_RATIO'][i] 
		#ratings['INTRINSIC_VALUE_NI'][i] = dataCalc['INTRINSIC_VALUE_NI'][i]
		#ratings['INTRINSIC_VALUE_EBIT'][i] = dataCalc['INTRINSIC_VALUE_EBIT'][i]
		#ratings['INTRINSIC_VALUE_FCF'][i] = dataCalc['INTRINSIC_VALUE_FCF'][i] 
		#ratings['MARGIN_OF_SAFETY_NI'][i] = dataCalc['MARGIN_OF_SAFETY_NI'][i] 
		#ratings['MARGIN_OF_SAFETY_EBIT'][i] = dataCalc['MARGIN_OF_SAFETY_EBIT'][i]
		#ratings['MARGIN_OF_SAFETY_FCF'][i] = dataCalc['MARGIN_OF_SAFETY_FCF'][i] 
		#ratings['DUPONT_SYSTEM_1'][i] = dataCalc['DUPONT_SYSTEM_1'][i] 
		#ratings['DUPONT_SYSTEM_2'][i] = dataCalc['DUPONT_SYSTEM_2'][i] 
		#ratings['RETENTION_RATIO'][i] = dataCalc['RETENTION_RATIO'][i] 
		#ratings['DIV_PAYOUT_RATIO'][i] = dataCalc['DIV_PAYOUT_RATIO'][i]
		#ratings['EARNINGS_YIELD'][i] = dataCalc['EARNINGS_YIELD'][i] 
		#ratings['DIVS_YIELD'][i] = dataCalc['DIVS_YIELD'][i] 
		#ratings['SGR'][i] = dataCalc['SGR'][i] 
		#ratings['DECISION'][i] = getRating(i, data, dataCalc)
		i += 1


	#print(ratings)
	filename = ratings['symbol']
	ToFile(path, filename, ratings)
	decorateFile(path, filename + ".json" )
	#getTickerObject()

	return ratings
#---------------------------------------------------
def getRating(year, data, dataCalc, sector):




	return Enums.Recommendation.STRONG_BUY.value
	#STRONG_BUY	= 5 
	#BUY		= 4
	#NEUTRAL	= 3
	#RISKY		= 2
	#AVOID		= 1
	#NA			= 0

#---------------------------------------------------
def unknown():
	return Enums.Rating.UNKNOWN.value

def halfToOne(ratioVal):

	if(ratioVal == None):
		return None

	if(ratioVal < 0.5):
		return Enums.Rating.AT_RISK.value
	elif(1 < ratioVal):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def onetoOneAndHalf(ratioVal):

	if(ratioVal == None):
		return None

	if(ratioVal < 1):
		return Enums.Rating.AT_RISK.value
	elif(1.5 < ratioVal):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value


def sectorRankUp(ratioVal, industry25, industry75):
	if(ratioVal == None or industry25 == None or industry75 == None):
		return None

	if(industry75 < ratioVal):
		return Enums.Rating.HEALTHY.value
	elif(ratioVal < industry25):
		return Enums.Rating.AT_RISK.value
	else:
		return Enums.Rating.QUESTIONABLE.value


def sectorRankDown(ratioVal, industry25, industry75):
	if(ratioVal == None or industry25 == None or industry75 == None):
		return None

	if(industry75 < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif(ratioVal < industry25):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def rateDebtRisk(ratioVal):
	if(ratioVal == None):
		return None

	if(0.80 < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif(ratioVal < 0.49):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def stLtDebtRisk(debtRatioVal, stLtDebtRatio, idebtRatioVal, idebtRatio25, idebtRatio75):
	if(debtRatioVal == None or stLtDebtRatio == None or idebtRatioVal == None or idebtRatio25 == None or idebtRatio75 == None):
		return None

	if( (idebtRatio75 / idebtRatioVal) < (stLtDebtRatio / debtRatioVal) ):
		return Enums.Rating.AT_RISK.value
	elif((stLtDebtRatio / debtRatioVal) < (idebtRatio25 / idebtRatioVal)):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def rateDebtEbitRatio(ratioVal):
	if(ratioVal == None):
		return None

	if(0.38 < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif(ratioVal < 0.28):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def rateFCCR(ratioVal):
	if(ratioVal == None):
		return None

	if(ratioVal < 1.25):
		return Enums.Rating.AT_RISK.value
	elif(2 < ratioVal):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def rateDegreeOfLeverage(ratioVal, currSales, prevSales, industryAvg):
	if(ratioVal == None or currSales == None or prevSales == None or industryAvg == None):
		return None

	if( chgSales < 0 and industryAvg < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif((0 < chgSales and industryAvg < ratioVal) or ratioVal < industryAvg):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.UNKNOWN.value


def rateFL(ratioVal):
	if(ratioVal == None):
		return None

	if(2 < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif(ratioVal < 1):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value



def rateEqMult1(ratioVal, ieqMult25, ieqMult75):
	if(ratioVal == None or ieqMult25 == None or ieqMult75 == None):
		return None

	if(ieqMult25 < ratioVal and ratioVal < ieqMult75):
		return Enums.Rating.HEALTHY.value
	elif(ieqMult75 < ratioVal):
		return Enums.Rating.AT_RISK.value
	else:
		return Enums.Rating.UNKNOWN.value

def rateCostOfDebt(ratioVal, ROIC):
	if(ratioVal == None):
		return None

	if(ratioVal < ROIC):
		return Enums.Rating.HEALTHY.value
	elif(ratioVal > Calcs.Basics.BaaBondYield() ):
		return Enums.Rating.AT_RISK.value
	else:
		return Enums.Rating.QUESTIONABLE.value

	




#def (ratioVal):
#	if(ratioVal == None):
#		return None

#	if( < ratioVal):
#		return Enums.Rating.AT_RISK
#	elif(ratioVal < ):
#		return Enums.Rating.HEALTHY
#	else:
#		return Enums.Rating.QUESTIONABLE




#-----------------------------------------------

#def (ratioVal):
#	if(ratioVal == None):
#		return None

#	if( < ratioVal):
#		return Enums.Rating.AT_RISK
#	elif(ratioVal < ):
#		return Enums.Rating.HEALTHY
#	else:
#		return Enums.Rating.QUESTIONABLE
