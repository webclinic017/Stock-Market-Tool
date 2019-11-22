import Calcs
import json
import inspect
import Reported
import instantiate
import yearly_price_service
import test_price_service
import sys

def getTickerObject():
	omit = "as_integer_ratio", "conjugate", "fromhex", "hex", "imag", "is_integer", "real"
	#print([x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ])
	return [x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ]

def ToFile(path, fileName, data):
	filePathNameExt = './' + path + '/' + fileName + 'Calc' + '.json'
	
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
#class priceData:
#	def getPrices(symbol, years):
#		prices = []
#		#Creates JSON objects for database:
#		i = 1
#		years = iter(years)
#		next(years)
#		for year in years:
#			#print(int(year))
#			try:
#				price = yearly_price_service.YearlyPriceService.get_avg_price(symbol, year, '../machine-learning/data/alpha-vantage/json-data/')
#				#print(price)
#				prices.append(price)
#			except:
##				print('Ticker not found!')
#				prices.append(-1)
#			i += 1

#		return prices
neg =  - (sys.maxsize -1)

def calculate(data):
	dataCalc = instantiate.instantiateDataCalc()
	unkept = []
	# Instantiate object.
	dataCalc['symbol'] = data['symbol']
	dataCalc['YEAR_INC']						= data['YEAR_INC']
	dataCalc['YEAR_BAL']						= data['YEAR_BAL']
	dataCalc['YEAR_CF']							= data['YEAR_CF']
	prices = test_price_service.getPrices(data['symbol'], dataCalc['YEAR_BAL'])
	
	i=1
	dataCalc['PRICE'][0] = Calcs.Names.PRICE
	while(i<34):
		dataCalc['PRICE'][i] = prices[i-1]
		i += 1
	i = 1
	# Independent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break

		# Basic Functions
		dataCalc['MARGINAL_TAX_RATE'][i] = Calcs.Basics.marginalTax()
		dataCalc['FAIR_RETURN_RATE'][i] = Calcs.Basics.grahamFairReturnRate()
		dataCalc['NO_GROWTH_PE'][i] = Calcs.Basics.noGrowthPe()
		dataCalc['GROWTH_MULTIPLE'][i] = Calcs.Basics.growthMultiple()
		dataCalc['REQUIRED_RETURN'][i] = Calcs.Basics.requiredReturn()
		dataCalc['AAA_BOND_YIELD'][i] = Calcs.Basics.aaaBondYield()
		dataCalc['REV_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(data['REV'][i], data['REV'][i+1]))
		dataCalc['NI_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(data['NI_INC'][i], data['NI_INC'][i+1]))
		dataCalc['COST_OF_SALES'][i] = Calcs.Basics.costOfSales(data['INV'][i], data['INV'][i+1], data['CHG_INVENTORIES'][i])
		dataCalc['WORKING_CAPITAL'][i] = Calcs.Basics.workingCapital(data['TOTAL_CURR_ASSETS'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['CAPITAL_EMPLOYED'][i] = Calcs.Basics.capitalEmployed(data['TOTAL_ASSETS1'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['TOTAL_INVEST'][i] = Calcs.Basics.totalInvestments(data['ST_INVEST'][i], data['LT_INVEST'][i])
		#if(data['ST_INVEST'][i] == 0 and data['LT_INVEST'][i] == 0):
			#dataCalc['TOTAL_INVEST'][i] = data['TOTAL_INVEST'][i]
		#else:
		dataCalc['TOTAL_DEBT'][i] = Calcs.Basics.totalDebt(data['ST_DEBT'][i], data['LT_DEBT'][i])
		dataCalc['EBIT'][i] = Calcs.Basics.ebit(data['NI_INC'][i], data['INT_EXP'][i], data['INC_TAX_EXPENSE'][i])
		dataCalc['EBIAT'][i] = Calcs.Basics.ebiat(dataCalc['EBIT'][i], data['DEPRE_AMORT'][i], data['ACC_DEPREC'][i])
		dataCalc['CAPEX'][i] = Calcs.Basics.capex(data['PPE'][i], data['PPE'][i+1], data['ACC_DEPREC'][i], data['ACC_DEPREC'][i+1])
		dataCalc['EBITDA'][i] = Calcs.Basics.ebitda(dataCalc['EBIT'][i], data['DEPRE_AMORT'][i])
		# Average Functions:			  
		dataCalc['AVG_RECEIVABLES'][i] = Calcs.Basics.avg(data['ACCTS_REC'][i], data['ACCTS_REC'][i+1])
		dataCalc['AVG_PAYABLES_ACCRUALS'][i] = Calcs.Basics.avg(data['PAYABLES_ACCRUALS'][i], data['PAYABLES_ACCRUALS'][i+1])
		dataCalc['AVG_INVENTORY'][i] = Calcs.Basics.avg(data['INV'][i], data['INV'][i+1])
		dataCalc['AVG_LT_ASSETS'][i] = Calcs.Basics.avg(data['TOTAL_NON_CURR_ASSETS'][i], data['TOTAL_NON_CURR_ASSETS'][i+1])
		dataCalc['AVG_ASSETS'][i] = Calcs.Basics.avg(data['TOTAL_ASSETS1'][i], data['TOTAL_ASSETS1'][i+1])
		dataCalc['AVG_LIABILITIES'][i] = Calcs.Basics.avg(data['TOTAL_LIAB'][i], data['TOTAL_LIAB'][i+1])
		dataCalc['AVG_EQUITY'][i] = Calcs.Basics.avg(data['TOTAL_EQUITY'][i], data['TOTAL_EQUITY'][i+1])
		# Solvency:						  
		dataCalc['CASH_RATIO'][i] = Calcs.Solvency.cashRatio(data['CASH_EQ'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['CASH_STI_RATIO'][i] = Calcs.Solvency.cashStiRatio(data['CASH_EQ_STI'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['CASH_SERVICE_RATIO'][i] = Calcs.Solvency.cashServiceRatio(data['CASH_EQ'][i], data['INT_EXP'][i])
		dataCalc['CASH_ST_DEBT_RATIO'][i] = Calcs.Solvency.cashStDebtRatio(data['CASH_EQ_STI'][i], data['ST_DEBT'][i])
		dataCalc['ACID_TEST'][i] = Calcs.Solvency.acidTest(data['CASH_EQ_STI'][i], data['ACCTS_REC'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['QUICK_RATIO'][i] = Calcs.Solvency.quickRatio(data['TOTAL_CURR_ASSETS'][i], data['INV'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['QUICK_RATIO_2'][i] = Calcs.Solvency.quickRatio2(data['TOTAL_CURR_ASSETS'][i], data['INV'][i], data['PREPAID_EXP'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['CURRENT_RATIO'][i] = Calcs.Solvency.currentRatio(data['TOTAL_CURR_ASSETS'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['NWC_TO_TA'][i] = Calcs.Solvency.netWorkingToTotalAssets(data['TOTAL_CURR_ASSETS'][i], data['TOTAL_CURR_LIAB'][i], data['TOTAL_ASSETS1'][i])
		# Capital Structure:		
		dataCalc['EQUITY_RATIO'][i] = Calcs.CapStructure.equityRatio(data['TOTAL_EQUITY'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i] = Calcs.CapStructure.equityMultiplier1(data['TOTAL_ASSETS1'][i], data['TOTAL_EQUITY'][i])
		# Asset Activity:
		dataCalc['SALES_TURNOVER'][i] = Calcs.Asset_Activity.salesTurnover( data['REV'][i], data['ACCTS_REC'][i])
		dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i] = Calcs.Asset_Activity.receivablesTurnover(data['ACCTS_REC'][i], data['CREDIT_SALES'][i])
		# Liability Activity:
		dataCalc['PAYABLES_TURNOVER_COGS'][i] = Calcs.Liab_Activity.payablesTurnoverCOGS(data['COGS'][i], data['PAYABLES'][i])
		dataCalc['DPO_COGS'][i] = Calcs.Liab_Activity.daysPayableOutstandingCOGS(dataCalc['PAYABLES_TURNOVER_COGS'][i])
		dataCalc['PAYABLES_TURNOVER_COS'][i] = Calcs.Liab_Activity.payablesTurnoverCOS( data['COST_OF_REV'][i], data['PAYABLES'][i])
		dataCalc['DPO_COS'][i] = Calcs.Liab_Activity.daysPayableOutstandingCOS(dataCalc['PAYABLES_TURNOVER_COS'][i])
		dataCalc['CHG_DEBT_REPAYMENT_REQ'][i] = Calcs.Liab_Activity.changeDebtObligations(data['ST_DEBT'][i], data['ST_DEBT'][i+1], data['CURR_LT_DEBT'][i], data['CURR_LT_DEBT'][i+1])
		# Profitability:
		dataCalc['ROS'][i] = Calcs.Profitability.returnOnSales(data['NI_INC'][i], data['REV'][i])
		dataCalc['ROE'][i] = Calcs.Profitability.returnOnEquity(data['NI_INC'][i], data['TOTAL_EQUITY'][i])
		dataCalc['ROA'][i] = Calcs.Profitability.returnOnAssets(data['NI_INC'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['EPS_DILUTED_NI'][i] = Calcs.Profitability.earningsPerShare(data['NI_INC'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['EPS_DILUTED_EBIT'][i] = Calcs.Profitability.earningsPerShare(dataCalc['EBIT'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['ROCE_NI'][i] = Calcs.Profitability.returnOnCapitalEmployedNI(data['NI_INC'][i], data['TOTAL_ASSETS1'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['PE'][i] = Calcs.Profitability.priceEarnings(dataCalc['PRICE'][i], data['DIL_WEIGHT_AVG_SHARES'][i], data['NI_INC'][i])
		dataCalc['GROSS_MARGIN'][i] = Calcs.Profitability.grossMarginRatio(data['PROFIT'][i], data['REV'][i])
		dataCalc['NOPAT_NI'][i] = Calcs.Profitability.netOperatingProfitAfterTaxNI(data['NI_INC'][i], data['NON_OP_INC_LOSS'][i], data['INT_EXP'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['OPERATING_RATIO'][i] = Calcs.Profitability.operatingRatio(data['OP_EXP'][i], data['REV'][i])
		dataCalc['OP_PROFIT_MARGIN'][i] = Calcs.Profitability.operatingProfitMargin(data['OP_INC_LOSS'][i], data['REV'][i])
		# Dividends:
		dataCalc['RETENTION_RATIO'][i] = Calcs.Dividends.retentionRatio(data['NI_INC'][i], data['DIVS_PAID'][i])
		dataCalc['DIV_PAYOUT_RATIO'][i] = Calcs.Dividends.dividendPayoutRatio(data['DIVS_PAID'][i], data['NI_INC'][i])
		
		i += 1

	i = 1
	# Compute Intermediate Averages:

	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break
		#Write recursive average Functions
		if(i < 30):
			dataCalc['AVG_NI_3YEAR'][i] = round(Calcs.Basics.threeYearAvg(data['NI_INC'][i], data['NI_INC'][i+1], data['NI_INC'][i+2]), 2) if (Calcs.Basics.threeYearAvg(data['NI_INC'][i], data['NI_INC'][i+1], data['NI_INC'][i+2]) != None) else None
		if(i < 30):
			dataCalc['AVG_EBIT_3YEAR'][i] = round(Calcs.Basics.threeYearAvg(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], dataCalc['EBIT'][i+2]), 2) if (Calcs.Basics.threeYearAvg(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], dataCalc['EBIT'][i+2]) != None) else None
		dataCalc['AVG_WORKING_CAPITAL'][i] = Calcs.Basics.avg(dataCalc['WORKING_CAPITAL'][i], dataCalc['WORKING_CAPITAL'][i+1])
		dataCalc['AVG_INVEST'][i] = Calcs.Basics.avg(dataCalc['TOTAL_INVEST'][i], dataCalc['TOTAL_INVEST'][i+1])
		dataCalc['AVG_DEBT'][i] = Calcs.Basics.avg(dataCalc['TOTAL_DEBT'][i], dataCalc['TOTAL_DEBT'][i+1])
		dataCalc['EBITDA_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EBITDA'][i], dataCalc['EBITDA'][i+1]))
		dataCalc['EBIT_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1]))
		dataCalc['EPS_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1]))
		dataCalc['NET_DEBT'][i] = Calcs.CapStructure.netDebt(dataCalc['TOTAL_DEBT'][i], data['CASH_EQ'][i])
		dataCalc['LEV_FCF'][i] = Calcs.Basics.leveredFreeCashFlow(data['NI_INC'][i], data['DEPRE_AMORT'][i], dataCalc['WORKING_CAPITAL'][i], dataCalc['WORKING_CAPITAL'][i+1], data['CURR_LT_DEBT'][i], data['ST_DEBT'][i])
		i += 1

	i = 1
	# Dependent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break

		# Basic Functions
		if(i < 30):
			dataCalc['AVG_LEV_FCF_3YEAR'][i] = round(Calcs.Basics.threeYearAvg(dataCalc['LEV_FCF'][i], dataCalc['LEV_FCF'][i+1], dataCalc['LEV_FCF'][i+2]), 2) if (Calcs.Basics.threeYearAvg(dataCalc['LEV_FCF'][i], dataCalc['LEV_FCF'][i+1], dataCalc['LEV_FCF'][i+2]) != None) else None
		
		dataCalc['UN_LEV_FCF'][i] = Calcs.Basics.unleveredFreeCashFlow(dataCalc['EBITDA'][i],  dataCalc['CAPEX'][i], dataCalc['WORKING_CAPITAL'][i], data['CURR_INC_TAX'][i])
		# Solvency:
		dataCalc['INT_SERVICE_RATIO'][i] = Calcs.Solvency.interestServiceRatio(dataCalc['EBIT'][i], data['INT_EXP'][i])
		if( dataCalc['MARGINAL_TAX_RATE'][i] != None):
			dataCalc['DEBT_SERVICE_RATIO'][i] = Calcs.Solvency.debtServiceCoverageRatio(dataCalc['EBIT'][i], data['INT_EXP'][i], data['ST_DEBT'][i], (dataCalc['MARGINAL_TAX_RATE'][i] / 100))
		# Capital Structure:
		dataCalc['CHG_ST_DEBT'][i] = Calcs.Basics.yoyChange(data['ST_DEBT'][i], data['ST_DEBT'][i+1])
		dataCalc['CHG_LT_DEBT'][i] = Calcs.Basics.yoyChange(data['LT_DEBT'][i], data['LT_DEBT'][i+1])
		dataCalc['CHG_NET_DEBT'][i] = Calcs.Basics.yoyChange(dataCalc['NET_DEBT'][i], dataCalc['NET_DEBT'][i+1])
		dataCalc['DEBT_RATIO'][i] = Calcs.CapStructure.debtRatio(dataCalc['TOTAL_DEBT'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['DEBT_EQ_RATIO'][i] = Calcs.CapStructure.debtEquityRatio(dataCalc['TOTAL_DEBT'][i], data['TOTAL_EQUITY'][i])
		dataCalc['TOTAL_CURR_LIAB_RATIO'][i] = Calcs.CapStructure.stDebtRatio(data['TOTAL_CURR_LIAB'][i], dataCalc['TOTAL_DEBT'][i])
		dataCalc['LT_DEBT_RATIO'][i] = Calcs.CapStructure.ltDebtRatio(data['LT_DEBT'][i], dataCalc['TOTAL_DEBT'][i])
		dataCalc['DEBT_TO_EBIT'][i] = Calcs.CapStructure.debtIncomeRatio(data['CURR_LT_DEBT'][i], data['NI_INC'][i])
		dataCalc['FIXED_CHARGE_COVERAGE'][i] = Calcs.CapStructure.fixedChargeCoverage(dataCalc['EBIT'][i], data['CHG_FIXED_INTANG'][i], data['INT_EXP'][i])
		dataCalc['DEGREE_COMBINED_LEV'][i] = Calcs.CapStructure.degreeCombinedLeverage(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1], data['REV'][i], data['REV'][i+1])
		dataCalc['DEGREE_OPERATING_LEV'][i] = Calcs.CapStructure.degreeOperatingLeverage(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], data['REV'][i], data['REV'][i+1])
		dataCalc['DEGREE_FINANCIAL_LEV'][i] = Calcs.CapStructure.degreeFinancialLeverage(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1], dataCalc['EBIT'][i], dataCalc['EBIT'][i+1])
		dataCalc['DFL_RATIO'][i] = Calcs.CapStructure.dflRatio(dataCalc['EBIT'][i], data['INT_EXP'][i])
		dataCalc['FINANCIAL_LEVERAGE'][i] = Calcs.CapStructure.financialLeverage(dataCalc['AVG_ASSETS'][i], dataCalc['AVG_EQUITY'][i])
		dataCalc['EQUITY_MULTIPLIER_RATIO_2'][i] = Calcs.CapStructure.equityMultiplier2(dataCalc['DEBT_RATIO'][i])
		dataCalc['NAV'][i] = Calcs.CapStructure.netAssetValue(data['TOTAL_ASSETS1'][i], data['TOTAL_LIAB'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['EFFECTIVE_INT_RATE'][i] = Calcs.CapStructure.effectiveInterestRate(data['INT_EXP'][i], dataCalc['TOTAL_DEBT'][i])
		if(dataCalc['MARGINAL_TAX_RATE'][i] != None):
			dataCalc['DEBT_COST_CAP'][i] = Calcs.CapStructure.debtCostCapital(dataCalc['EFFECTIVE_INT_RATE'][i], (dataCalc['MARGINAL_TAX_RATE'][i] / 100))
		if(dataCalc['FAIR_RETURN_RATE'][i] != None and dataCalc['EFFECTIVE_INT_RATE'][i] != None and dataCalc['MARGINAL_TAX_RATE'][i] != None):
			dataCalc['WACC'][i] = Calcs.CapStructure.wacc(data['TOTAL_EQUITY'][i], dataCalc['TOTAL_DEBT'][i], (dataCalc['FAIR_RETURN_RATE'][i] / 100), (dataCalc['EFFECTIVE_INT_RATE'][i] / 100), (dataCalc['MARGINAL_TAX_RATE'][i] / 100))
		# Asset Activity:
		dataCalc['DSO'][i] = Calcs.Asset_Activity.daysSalesOutstanding(dataCalc['SALES_TURNOVER'][i])
		dataCalc['ASSET_TURNOVER'][i] = Calcs.Asset_Activity.assetTurnover(data['REV'][i], dataCalc['AVG_ASSETS'][i])
		dataCalc['ASSET_TURN_RATE'][i] = Calcs.Asset_Activity.assetTurnoverRate(dataCalc['ASSET_TURNOVER'][i])
		dataCalc['LT_ASSET_TURNOVER'][i] = Calcs.Asset_Activity.longTermAssetTurnover(dataCalc['AVG_LT_ASSETS'][i], data['REV'][i])
		dataCalc['LT_ASSET_TURN_RATE'][i] = Calcs.Asset_Activity.longTermAssetTurnoverRate(dataCalc['LT_ASSET_TURNOVER'][i])
		dataCalc['INV_SALES_TURNOVER'][i] = Calcs.Asset_Activity.inventorySalesTurnover( data['REV'][i], dataCalc['AVG_INVENTORY'][i])
		dataCalc['DSI'][i] = Calcs.Asset_Activity.daysSalesInventory(dataCalc['INV_SALES_TURNOVER'][i])
		dataCalc['INV_COGS_TURNOVER'][i] = Calcs.Asset_Activity.inventoryCOGSTurnover(data['COGS'][i], dataCalc['AVG_INVENTORY'][i])
		dataCalc['DIO'][i] = Calcs.Asset_Activity.daysInventoryOutstanding(dataCalc['INV_COGS_TURNOVER'][i])
		dataCalc['DRO'][i] = Calcs.Asset_Activity.daysReceivablesOutstanding(dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i])
		dataCalc['WORKING_CAP_TURNOVER'][i] = Calcs.Asset_Activity.workingCapitalTurnover(data['REV'][i], dataCalc['AVG_WORKING_CAPITAL'][i])
		dataCalc['DWC'][i] = Calcs.Asset_Activity.daysWorkingCapital(dataCalc['WORKING_CAP_TURNOVER'][i])
		dataCalc['ROI_INVESTMENTS'][i] = Calcs.Asset_Activity.investmentsROI(data['CASH_INVEST_ACT1'][i], dataCalc['AVG_INVEST'][i])
		# Liability Activity:
		dataCalc['CREDITORS_TURNOVER'][i] = Calcs.Liab_Activity.CreditorsTurnover(dataCalc['AVG_RECEIVABLES'][i], data['CREDIT_SALES'][i])
		dataCalc['CDO'][i] = Calcs.Liab_Activity.CreditorsDaysOutstanding(dataCalc['CREDITORS_TURNOVER'][i])
		dataCalc['LIAB_TURNOVER'][i] = Calcs.Liab_Activity.liabitiesTurnover(data['REV'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['LIAB_TURN_RATE'][i] = Calcs.Liab_Activity.liabitiesTurnoverRate(dataCalc['LIAB_TURNOVER'][i])
		dataCalc['DEBTORS_PAYBACK_PERIOD'][i] = Calcs.Liab_Activity.debtorsPaybackPeriod(dataCalc['AVG_DEBT'][i], data['CASH_REPAY_DEBT'][i])
		dataCalc['BURN_RATE'][i] = Calcs.Liab_Activity.burnRate(data['CASH_EQ_STI'][i], dataCalc['EBIT'][i])
		# Profitability
		dataCalc['CCC'][i] = Calcs.Profitability.cashConversionCycle(dataCalc['DIO'][i], dataCalc['DSO'][i], dataCalc['DPO_COGS'][i])
		dataCalc['ROCE_EBIT'][i] = Calcs.Profitability.returnOnCapitalEmployedEBIT(dataCalc['EBIT'][i], data['TOTAL_ASSETS1'][i], data['TOTAL_CURR_LIAB'][i])
		if(i < 30):
			dataCalc['PE_REL_3'][i] = Calcs.Profitability.priceEarnings3(dataCalc['PE'][i], dataCalc['PE'][i+1], dataCalc['PE'][i+2])
		if(i < 30):
			dataCalc['PE_REL_5'][i] = Calcs.Profitability.priceEarnings5(dataCalc['PE'][i], dataCalc['PE'][i+1], dataCalc['PE'][i+2], dataCalc['PE'][i+3], dataCalc['PE'][i+4])
		dataCalc['EARNINGS_POWER'][i] = Calcs.Profitability.earningsPower(dataCalc['EBIT'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['ROIC'][i] = Calcs.Profitability.returnOnInvestedCapital(dataCalc['NOPAT_NI'][i], dataCalc['TOTAL_INVEST'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		if(dataCalc['MARGINAL_TAX_RATE'][i] != None):
			dataCalc['NOPAT_EBIT'][i] = Calcs.Profitability.netOperatingProfitAfterTaxEBIT(data['OP_INC_LOSS'][i], (dataCalc['MARGINAL_TAX_RATE'][i] / 100), data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['DUPONT_SYSTEM_1'][i] = Calcs.Profitability.dupontSystem_1(dataCalc['ROS'][i], dataCalc['ASSET_TURNOVER'][i], dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i])

		# Valuation Measures:
		dataCalc['MV'][i] = Calcs.Valuations.marketCap(dataCalc['PRICE'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['MV_EBIT_RATIO'][i] = Calcs.Valuations.ebitToMv(dataCalc['EBIT'][i], dataCalc['MV'][i])
		dataCalc['ORIG_GRAHAM'][i] = Calcs.Valuations.originalGraham(dataCalc['EPS_DILUTED_NI'][i], dataCalc['NO_GROWTH_PE'][i], dataCalc['GROWTH_MULTIPLE'][i], dataCalc['EPS_GROWTH_RATE'][i])
		dataCalc['REVISED_GRAHAM'][i] = Calcs.Valuations.revisedGraham(dataCalc['EPS_DILUTED_NI'][i], dataCalc['NO_GROWTH_PE'][i], dataCalc['GROWTH_MULTIPLE'][i], dataCalc['EPS_GROWTH_RATE'][i], dataCalc['REQUIRED_RETURN'][i], dataCalc['AAA_BOND_YIELD'][i])
		dataCalc['EV'][i] = Calcs.Valuations.enterpriseValue(dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ_STI'][i])
		dataCalc['EV_EBIT'][i] = Calcs.Valuations.enterpriseValueEBIT(dataCalc['EBIT'][i], dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ_STI'][i])
		dataCalc['EV_NI'][i] = Calcs.Valuations.enterpriseValueNI(data['NI_INC'][i], dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ_STI'][i])
		dataCalc['BV'][i] = Calcs.Valuations.bookValue(data['TOTAL_ASSETS1'][i], data['TOTAL_INTANG_ASSETS'][i], data['TOTAL_LIAB'][i+1])
		dataCalc['BV_PER_SHARE'][i] = Calcs.Valuations.bookValuePerShare(dataCalc['BV'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['BV_NI'][i] = Calcs.Valuations.bookValueNIperShare(dataCalc['EPS_DILUTED_NI'][i], dataCalc['BV_PER_SHARE'][i])
		dataCalc['BV_EBIT'][i] = Calcs.Valuations.bookValueEBITperShare(dataCalc['EPS_DILUTED_EBIT'][i], dataCalc['BV_PER_SHARE'][i])
		dataCalc['PRICE_SALES'][i] = Calcs.Valuations.priceToSalesPerShare(dataCalc['PRICE'][i], data['REV'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['PRICE_BOOK'][i] = Calcs.Valuations.priceToBookPerShare(dataCalc['PRICE'][i], dataCalc['BV'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['PRICE_NAV'][i] = Calcs.Valuations.priceToNAVPerShare(dataCalc['PRICE'][i], dataCalc['NAV'][i])
		dataCalc['PRICE_FCF'][i] = Calcs.Valuations.pricetoLeveredFreeCashFlowPerShare(dataCalc['PRICE'][i], dataCalc['LEV_FCF'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['PRICE_UN_FCF'][i] = Calcs.Valuations.priceToUnLeveredFreeCashFlowPerShare(dataCalc['PRICE'][i], dataCalc['UN_LEV_FCF'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['MV_OCF'][i] = Calcs.Valuations.ocfToMv(dataCalc['EBIT'][i], dataCalc['MV'][i])
		dataCalc['CASH_PRICE_RATIO'][i] = Calcs.Valuations.cashPriceRatio(data['CASH_EQ_STI'][i], dataCalc['MV'][i])
		
		tempNi3Year = neg
		if(dataCalc['AVG_NI_3YEAR'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != 0 ):
			tempNi3Year = dataCalc['AVG_NI_3YEAR'][i] / data['DIL_WEIGHT_AVG_SHARES'][i]
		else:
			tempNi3Year = None

		tempEbit3Year = neg
		if(dataCalc['AVG_EBIT_3YEAR'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != 0 ):
			tempEbit3Year = dataCalc['AVG_EBIT_3YEAR'][i] / data['DIL_WEIGHT_AVG_SHARES'][i]
		else:
			tempEbit3Year = None
		
		tempFcf3Year = neg
		if(dataCalc['AVG_LEV_FCF_3YEAR'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != None and data['DIL_WEIGHT_AVG_SHARES'][i] != 0 ):
			tempFcf3Year = dataCalc['AVG_LEV_FCF_3YEAR'][i] / data['DIL_WEIGHT_AVG_SHARES'][i]
		else:
			tempFcf3Year = None
		if(dataCalc['WACC'][i] != None):
			dataCalc['INTRINSIC_VALUE_NI'][i] = Calcs.Valuations.intrinsicValueNI(0, tempNi3Year, (dataCalc['WACC'][i] / 100), 1)
			dataCalc['INTRINSIC_VALUE_EBIT'][i] = Calcs.Valuations.intrinsicValueEBIT(0, tempEbit3Year, (dataCalc['WACC'][i] / 100), 1)
			dataCalc['INTRINSIC_VALUE_FCF'][i] = Calcs.Valuations.intrinsicValueFCF(0, tempFcf3Year, (dataCalc['WACC'][i] / 100), 1)
		dataCalc['MARGIN_OF_SAFETY_NI'][i] = Calcs.Valuations.marginOfSafety_NI(dataCalc['INTRINSIC_VALUE_NI'][i], dataCalc['PRICE'][i])
		dataCalc['MARGIN_OF_SAFETY_EBIT'][i] = Calcs.Valuations.marginOfSafety_EBIT(dataCalc['INTRINSIC_VALUE_EBIT'][i], dataCalc['PRICE'][i])
		dataCalc['MARGIN_OF_SAFETY_FCF'][i] = Calcs.Valuations.marginOfSafety_FCF(dataCalc['INTRINSIC_VALUE_FCF'][i], dataCalc['PRICE'][i])
		# Dividends: 
		dataCalc['EARNINGS_YIELD'][i] = Calcs.Dividends.earningsYieldRatio(data['NI_INC'][i], dataCalc['MV'][i])
		dataCalc['DIVS_YIELD'][i] = Calcs.Dividends.dividendYieldRatio(data['DIVS_PAID'][i], dataCalc['MV'][i])
		dataCalc['SGR'][i] = Calcs.Dividends.sustainableGrowthRate(dataCalc['ROE'][i], dataCalc['RETENTION_RATIO'][i])
		
		i += 1
		
	#print(dataCalc)
	filename = dataCalc['symbol']
	ToFile(path, filename, dataCalc)
	decorateFile(path, filename + ".json" )
	getTickerObject()

	return dataCalc

