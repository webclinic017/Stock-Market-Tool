import Enums
import instantiate
import Calcs
import json
import inspect
import numpy as np
import sys

twoThirds = 66.66
oneThird = 33.33
mid = 50
neg =  - (sys.maxsize -1)

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


def genRatings(dataFile, dataCalcFile, industry):
	
	with open(dataFile) as json_file:
		data = json.load(json_file)
	with open(dataCalcFile) as json_file:
		dataCalc = json.load(json_file)

	ratings = instantiate.instantiateDataCalc()
	ratings['SECTOR'] = industry['SECTOR']
	ratings['symbol'] = dataCalc['symbol']
	ratings['DECISION'] = [0] * 35
	ratings['DECISION'] = [None] * 35
	ratings['DECISION'][0] = "Evaluation Decision"

	i = 1
	# Dependent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print(dataCalc['symbol'], "Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break
		ratings['CASH_RATIO'][i] = halfToOne(dataCalc['CASH_RATIO'][i])
		ratings['CASH_STI_RATIO'][i] = halfToOne(dataCalc['CASH_STI_RATIO'][i]) #!Important
		ratings['CASH_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['CASH_SERVICE_RATIO'][i])
		ratings['INT_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['INT_SERVICE_RATIO'][i])
		ratings['CASH_ST_DEBT_RATIO'][i] = halfToOne(dataCalc['CASH_ST_DEBT_RATIO'][i])
		ratings['ACID_TEST'][i] = onetoOneAndHalf(dataCalc['ACID_TEST'][i])
		ratings['QUICK_RATIO'][i] = onetoOneAndHalf(dataCalc['QUICK_RATIO'][i])
		ratings['QUICK_RATIO_2'][i] = onetoOneAndHalf(dataCalc['QUICK_RATIO_2'][i])
		ratings['CURRENT_RATIO'][i] = onetoOneAndHalf(dataCalc['CURRENT_RATIO'][i])
		ratings['NWC_TO_TA'][i] = sectorRankUp(dataCalc['NWC_TO_TA'][i], industry['NWC_TO_TA'][i])
		ratings['DEBT_SERVICE_RATIO'][i] = onetoOneAndHalf(dataCalc['DEBT_SERVICE_RATIO'][i])
		ratings['NET_DEBT'][i] = unknown() #Compare against sector on per share basis
		ratings['DEBT_RATIO'][i] = rateDebtRisk(dataCalc['DEBT_RATIO'][i]) #Note: equation is same math as EQUITY_MULTIPLIER_RATIO_2
		ratings['DEBT_EQ_RATIO'][i] = sectorRankDown(dataCalc['DEBT_EQ_RATIO'][i], industry['DEBT_EQ_RATIO'][i])
		ratings['DEBT_TO_EBIT'][i] = rateDebtEbitRatio(dataCalc['DEBT_TO_EBIT'][i])
		ratings['FIXED_CHARGE_COVERAGE'][i] = rateFCCR(dataCalc['FIXED_CHARGE_COVERAGE'][i])
		ratings['DEGREE_COMBINED_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_COMBINED_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_COMBINED_LEV'][i])
		ratings['DEGREE_OPERATING_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_OPERATING_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_OPERATING_LEV'][i])
		ratings['DEGREE_FINANCIAL_LEV'][i] = rateDegreeOfLeverage(dataCalc['DEGREE_FINANCIAL_LEV'][i], data['REV'][i], data['REV'][i+1], industry['DEGREE_FINANCIAL_LEV'][i])
		ratings['DFL_RATIO'][i] = rateDegreeOfLeverage(dataCalc['DFL_RATIO'][i], data['REV'][i], data['REV'][i+1], industry['DFL_RATIO'][i])
		ratings['FINANCIAL_LEVERAGE'][i] = rateFL(dataCalc['FINANCIAL_LEVERAGE'][i])
		ratings['EQUITY_RATIO'][i] = sectorRankUp(dataCalc['EQUITY_RATIO'][i], industry['EQUITY_RATIO'][i])
		ratings['EQUITY_MULTIPLIER_RATIO_1'][i] = sectorRankMidLower(dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i], industry['EQUITY_MULTIPLIER_RATIO_1'][i])
		ratings['EQUITY_MULTIPLIER_RATIO_2'][i] = rateDebtRisk(dataCalc['DEBT_RATIO'][i]) #Note: equation is same math as DEBT_RATIO
		ratings['NAV'][i] = unknown() #Compare against sector
		ratings['EFFECTIVE_INT_RATE'][i] = rateCostOfDebt(dataCalc['EFFECTIVE_INT_RATE'][i], dataCalc['ROCE_EBIT'][i])
		ratings['DEBT_COST_CAP'][i] = rateCostOfDebt(dataCalc['DEBT_COST_CAP'][i], dataCalc['ROCE_NI'][i])
		ratings['WACC'][i] = sectorRankDown(dataCalc['WACC'][i], industry['WACC'][i]) #Important
		ratings['SALES_TURNOVER'][i] = sectorRankUp(dataCalc['SALES_TURNOVER'][i], industry['SALES_TURNOVER'][i])
		ratings['DSO'][i] = sectorRankDown(dataCalc['DSO'][i], industry['DSO'][i])
		ratings['ASSET_TURNOVER'][i] = sectorRankUp(dataCalc['ASSET_TURNOVER'][i], industry['ASSET_TURNOVER'][i])
		ratings['ASSET_TURN_RATE'][i] = sectorRankUp(dataCalc['ASSET_TURN_RATE'][i], industry['ASSET_TURN_RATE'][i])
		ratings['LT_ASSET_TURNOVER'][i] = sectorRankUp(dataCalc['LT_ASSET_TURNOVER'][i], industry['LT_ASSET_TURNOVER'][i])
		ratings['LT_ASSET_TURN_RATE'][i] = sectorRankUp(dataCalc['LT_ASSET_TURN_RATE'][i], industry['LT_ASSET_TURN_RATE'][i])
		ratings['INV_SALES_TURNOVER'][i] = sectorRankUp(dataCalc['INV_SALES_TURNOVER'][i], industry['INV_SALES_TURNOVER'][i])
		ratings['DSI'][i] = sectorRankDown(dataCalc['DSI'][i], industry['DSI'][i])
		ratings['INV_COGS_TURNOVER'][i] = sectorRankUp(dataCalc['INV_COGS_TURNOVER'][i], industry['INV_COGS_TURNOVER'][i])
		ratings['DIO'][i] = sectorRankDown(dataCalc['DIO'][i], industry['DIO'][i])
		ratings['RECEIVABLES_ACCTS_TURNOVER'][i] = sectorRankUp(dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i], industry['RECEIVABLES_ACCTS_TURNOVER'][i])
		ratings['DRO'][i] = sectorRankDown(dataCalc['DRO'][i], industry['DRO'][i])
		ratings['WORKING_CAP_TURNOVER'][i] = sectorRankUp(dataCalc['WORKING_CAP_TURNOVER'][i], industry['WORKING_CAP_TURNOVER'][i])
		ratings['DWC'][i] = sectorRankDown(dataCalc['DWC'][i], industry['DWC'][i])
		ratings['ROI_INVESTMENTS'][i] =  sectorRankUp(dataCalc['ROI_INVESTMENTS'][i], industry['ROI_INVESTMENTS'][i])
		ratings['CREDITORS_TURNOVER'][i] =  sectorRankUp(dataCalc['CREDITORS_TURNOVER'][i], industry['CREDITORS_TURNOVER'][i])
		ratings['CDO'][i] = sectorRankDown(dataCalc['CDO'][i], industry['CDO'][i])
		ratings['PAYABLES_TURNOVER_COGS'][i] = sectorRankDown(dataCalc['PAYABLES_TURNOVER_COGS'][i], industry['PAYABLES_TURNOVER_COGS'][i]) #Improve with rate of change 
		ratings['PAYABLES_TURNOVER_COS'][i] = sectorRankDown(dataCalc['PAYABLES_TURNOVER_COS'][i], industry['PAYABLES_TURNOVER_COS'][i]) #Improve with rate of change 
		ratings['DPO_COGS'][i] = sectorRankMidLower(dataCalc['DPO_COGS'][i], industry['DPO_COGS'][i]) 
		ratings['DPO_COS'][i] = sectorRankMidLower(dataCalc['DPO_COS'][i], industry['DPO_COS'][i]) 
		ratings['LIAB_TURNOVER'][i] = sectorRankUp(dataCalc['LIAB_TURNOVER'][i], industry['LIAB_TURNOVER'][i])
		ratings['LIAB_TURN_RATE'][i] = sectorRankDown(dataCalc['LIAB_TURN_RATE'][i], industry['LIAB_TURN_RATE'][i])
		ratings['CHG_DEBT_REPAYMENT_REQ'][i] = sectorRankDown(dataCalc['CHG_DEBT_REPAYMENT_REQ'][i], industry['CHG_DEBT_REPAYMENT_REQ'][i])
		ratings['DEBTORS_PAYBACK_PERIOD'][i] = sectorRankDown(dataCalc['DEBTORS_PAYBACK_PERIOD'][i], industry['DEBTORS_PAYBACK_PERIOD'][i])
		ratings['BURN_RATE'][i] = rateBurnRate(dataCalc['BURN_RATE'][i])  #!Important
		ratings['CCC'][i] = rateCCC(dataCalc['CCC'][i], industry['CCC'][i])  #!Important
		ratings['ROS'][i] = sectorRankUp(dataCalc['ROS'][i], industry['ROS'][i])
		ratings['ROE'][i] = sectorRankUp(dataCalc['ROE'][i], industry['ROE'][i]) 
		ratings['ROA'][i] = sectorRankUp(dataCalc['ROA'][i], industry['ROA'][i]) 
		ratings['ROCE_NI'][i] = sectorRankUp(dataCalc['ROCE_NI'][i], industry['ROCE_NI'][i])
		ratings['EPS_DILUTED_NI'][i] = sectorRankUp(dataCalc['EPS_DILUTED_NI'][i], industry['EPS_DILUTED_NI'][i])
		ratings['EPS_DILUTED_EBIT'][i] = sectorRankUp(dataCalc['EPS_DILUTED_EBIT'][i], industry['EPS_DILUTED_EBIT'][i])
		ratings['ROCE_EBIT'][i] = sectorRankUp(dataCalc['ROCE_EBIT'][i], industry['ROCE_EBIT'][i]) 
		ratings['PE'][i] = sectorRankDown(dataCalc['PE'][i], industry['PE'][i]) 
		ratings['PE_REL_3'][i] = sectorRankDown(dataCalc['PE_REL_3'][i], industry['PE_REL_3'][i])  #!Important
		ratings['PE_REL_5'][i] = sectorRankDown(dataCalc['PE_REL_5'][i], industry['PE_REL_5'][i]) 
		ratings['EARNINGS_POWER'][i] = sectorRankUp(dataCalc['EARNINGS_POWER'][i], industry['EARNINGS_POWER'][i]) #!Important
		ratings['GROSS_MARGIN'][i] = sectorRankUp(dataCalc['GROSS_MARGIN'][i], industry['GROSS_MARGIN'][i])
		ratings['NOPAT_NI'][i] = sectorRankUp(dataCalc['NOPAT_NI'][i], industry['NOPAT_NI'][i])
		ratings['NOPAT_EBIT'][i] = sectorRankUp(dataCalc['NOPAT_EBIT'][i], industry['NOPAT_EBIT'][i])
		ratings['ROIC'][i] = sectorRankUp(dataCalc['ROIC'][i], industry['ROIC'][i])
		ratings['OPERATING_RATIO'][i] = sectorRankDown(dataCalc['OPERATING_RATIO'][i], industry['OPERATING_RATIO'][i])
		ratings['OP_PROFIT_MARGIN'][i] = sectorRankUp(dataCalc['OP_PROFIT_MARGIN'][i], industry['OP_PROFIT_MARGIN'][i])
		ratings['MV'][i] = unknown() 
		ratings['MV_EBIT_RATIO'][i] = sectorRankUp(dataCalc['MV_EBIT_RATIO'][i], industry['MV_EBIT_RATIO'][i])
		ratings['ORIG_GRAHAM'][i] =  unknown() 
		ratings['REVISED_GRAHAM'][i] =  unknown() 
		ratings['EV'][i] = unknown()
		ratings['EV_EBIT'][i] = sectorRankUp(dataCalc['EV_EBIT'][i], industry['EV_EBIT'][i])
		ratings['EV_NI'][i] = sectorRankUp(dataCalc['EV_NI'][i], industry['EV_NI'][i])
		ratings['BV'][i] = unknown()
		ratings['BV_PER_SHARE'][i] =  sectorRankUp(dataCalc['BV_PER_SHARE'][i], industry['BV_PER_SHARE'][i])
		ratings['BV_NI'][i] = sectorRankUp(dataCalc['BV_NI'][i], industry['BV_NI'][i])
		ratings['BV_EBIT'][i] = sectorRankUp(dataCalc['BV_EBIT'][i], industry['BV_EBIT'][i])
		ratings['PRICE_SALES'][i] = sectorRankUp(dataCalc['PRICE_SALES'][i], industry['PRICE_SALES'][i])
		ratings['PRICE_BOOK'][i] = sectorRankUp(dataCalc['PRICE_BOOK'][i], industry['PRICE_BOOK'][i])
		ratings['PRICE_NAV'][i] = sectorRankUp(dataCalc['PRICE_NAV'][i], industry['PRICE_NAV'][i])
		ratings['PRICE_FCF'][i] = sectorRankUp(dataCalc['PRICE_FCF'][i], industry['PRICE_FCF'][i])
		ratings['PRICE_UN_FCF'][i] = sectorRankUp(dataCalc['PRICE_UN_FCF'][i], industry['PRICE_UN_FCF'][i])
		ratings['MV_OCF'][i] = sectorRankUp(dataCalc['MV_OCF'][i], industry['MV_OCF'][i])
		ratings['CASH_PRICE_RATIO'][i] = sectorRankUp(dataCalc['CASH_PRICE_RATIO'][i], industry['CASH_PRICE_RATIO'][i])
		ratings['INTRINSIC_VALUE_NI'][i] = unknown()
		ratings['INTRINSIC_VALUE_EBIT'][i] = unknown()
		ratings['INTRINSIC_VALUE_FCF'][i] = unknown()
		ratings['MARGIN_OF_SAFETY_NI'][i] = rateMarginOfSafety(dataCalc['MARGIN_OF_SAFETY_NI'][i], industry['MARGIN_OF_SAFETY_NI'][i])
		ratings['MARGIN_OF_SAFETY_EBIT'][i] = sectorRankUp(dataCalc['MARGIN_OF_SAFETY_EBIT'][i], industry['MARGIN_OF_SAFETY_EBIT'][i])
		ratings['MARGIN_OF_SAFETY_FCF'][i] = sectorRankUp(dataCalc['MARGIN_OF_SAFETY_FCF'][i], industry['MARGIN_OF_SAFETY_FCF'][i])
		ratings['DUPONT_SYSTEM_1'][i] = sectorRankUp(dataCalc['DUPONT_SYSTEM_1'][i], industry['DUPONT_SYSTEM_1'][i])
		ratings['RETENTION_RATIO'][i] = sectorRankUp(dataCalc['RETENTION_RATIO'][i], industry['RETENTION_RATIO'][i])
		ratings['DIV_PAYOUT_RATIO'][i] = sectorRankUp(dataCalc['DIV_PAYOUT_RATIO'][i], industry['DIV_PAYOUT_RATIO'][i])
		ratings['EARNINGS_YIELD'][i] = sectorRankUp(dataCalc['EARNINGS_YIELD'][i], industry['EARNINGS_YIELD'][i])
		ratings['DIVS_YIELD'][i] = sectorRankUp(dataCalc['DIVS_YIELD'][i], industry['DIVS_YIELD'][i])
		ratings['SGR'][i] = sectorRankUp(dataCalc['SGR'][i], industry['SGR'][i]) 
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
	return None

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


def sectorRankUp(ratioVal, industryVals):
	if(ratioVal == None):
		return None

	vals = [neg]
	vals = []

	for item in industryVals:
		if(item != None):
			vals.append(item)

	lowerThird = np.percentile(vals, oneThird)
	upperThird = np.percentile(vals, twoThirds) 

	if(upperThird < ratioVal):
		return Enums.Rating.HEALTHY.value
	elif(ratioVal < lowerThird):
		return Enums.Rating.AT_RISK.value
	else:
		return Enums.Rating.QUESTIONABLE.value

def sectorRankMidLower(ratioVal, industryVals):
	if(ratioVal == None):
		return None

	vals = [neg]
	vals = []

	for item in industryVals:
		if(item != None):
			vals.append(item)

	lowerThird = np.percentile(vals, oneThird)
	upperThird = np.percentile(vals, twoThirds) 

	if(upperThird < ratioVal):
		return Enums.Rating.QUESTIONABLE.value
	else:
		return Enums.Rating.HEALTHY.value

def sectorRankDown(ratioVal, industryVals):
	if(ratioVal == None):
		return None

	vals = [neg]
	vals = []

	for item in industryVals:
		if(item != None):
			vals.append(item)

	lowerThird = np.percentile(vals, oneThird)
	upperThird = np.percentile(vals, twoThirds) 

	if(upperThird < ratioVal):
		return Enums.Rating.AT_RISK.value
	elif(ratioVal < lowerThird):
		return Enums.Rating.HEALTHY.value
	else:
		return Enums.Rating.QUESTIONABLE.value

#def sectorRankRateOfChangeDown(ratioVal, prevRatioVal, industryVals, prevIndustryVals):
#	if(ratioVal == None or prevRatioVal == None):
#		return None

#	vals = [neg]
#	vals = []	
#	prevVals = [neg]
#	prevVals = []

#	for item in industryVals:
#		if(item != None or item != "nan"):
#			vals.append(item)
#	for item in prevIndustryVals:
#		if(item != None or item != "nan"):
#			prevVals.append(item)

#	lowerThird = np.percentile(vals, oneThird)
#	upperThird = np.percentile(vals, twoThirds) 
	
#	prevLowerThird = np.percentile(prevVals, oneThird)
#	prevUpperThird = np.percentile(prevVals, twoThirds) 
	
#	if( (upperThird - prevUpperThird)):
#		return Enums.Rating.UNKNOWN.value
#	print(ratioVal, prevRatioVal, upperThird, prevUpperThird, (ratioVal - prevRatioVal) / (upperThird - prevUpperThird))


#	if(upperThird < (ratioVal - prevRatioVal) / (upperThird - prevUpperThird) ):
#		return Enums.Rating.AT_RISK.value

#	if(lowerThird - prevLowerThird):
#		return Enums.Rating.UNKNOWN.value
	

#	elif((ratioVal - prevRatioVal) / (lowerThird - prevLowerThird) < lowerThird):
#		return Enums.Rating.HEALTHY.value
#	else:
#		return Enums.Rating.QUESTIONABLE.value

def rateMarginOfSafety(ratioVal, industryVals):
	if(ratioVal == None):
		return None

	if(ratioVal < 0):
		return Enums.Rating.AT_RISK.value

	vals = [neg]
	vals = []

	for item in industryVals:
		if(item != None):
			vals.append(item)

	lowerThird = np.percentile(vals, oneThird)
	upperThird = np.percentile(vals, twoThirds) 

	if(upperThird < ratioVal):
		return Enums.Rating.HEALTHY.value
	elif(ratioVal < lowerThird):
		return Enums.Rating.AT_RISK.value
	else:
		return Enums.Rating.QUESTIONABLE.value


def rateCCC(value, industryVals):
	if(value == None):
		return None

	if(value < 30):
		return Enums.Rating.HEALTHY.value

	sectorRankDown(value, industryVals)


def rateBurnRate(ratioVal):
	if(ratioVal == None):
		return Enums.Rating.HEALTHY.value
	elif(ratioVal < 1):
		return Enums.Rating.AT_RISK.value
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

def rateDegreeOfLeverage(ratioVal, currSales, prevSales, industryVals):
	if(ratioVal == None or currSales == None or prevSales == None):
		return None
	
	vals = [neg]
	vals = []

	for item in industryVals:
		if(item != None):
			vals.append(item)

	chgSales = currSales - prevSales
	industryAvg = np.percentile(vals, mid)

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

