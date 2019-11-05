import Calcs
import json
import inspect
import Reported
import instantiate

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
	

def calculate(data):
	dataCalc = instantiate.instantiateDataCalc(data)
	unkept = []

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
		#if(data['ST_INVEST'][i] == 0 and data['LT_INVEST'][i] == 0):
			#dataCalc['TOTAL_INVEST'][i] = data['TOTAL_INVEST'][i]
		#else:
		dataCalc['TOTAL_INVEST'][i] = Calcs.Basics.totalInvestments(data['ST_INVEST'][i], data['LT_INVEST'][i])
		dataCalc['TOTAL_DEBT'][i] = Calcs.Basics.totalDebt(data['ST_DEBT'][i], data['LT_DEBT'][i])
		dataCalc['EBIT'][i] = Calcs.Basics.ebit(data['NI_INC'][i], data['INT_EXP'][i], data['INC_TAX_EXPENSE'][i])
		dataCalc['EBIAT'][i] = Calcs.Basics.ebiat(dataCalc['EBIT'][i], data['DEPRE_AMORT'][i], data['ACC_DEPREC'][i])
		dataCalc['EBITDA'][i] = Calcs.Basics.ebitda(dataCalc['EBIT'][i], data['DEPRE_AMORT'][i])
		dataCalc['CAPEX'][i] = Calcs.Basics.capex(data['PPE'][i], data['PPE'][i+1], data['ACC_DEPREC'][i])
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
		dataCalc['CASH_SERVICE_RATIO'][i] = Calcs.Solvency.cashServiceRatio(data['CASH_EQ'][i], data['INT_EXP'][i])
		dataCalc['CASH_COVERAGE_RATIO'][i] = Calcs.Solvency.cashCoverageRatio(data['CASH_EQ'][i], data['ST_DEBT'][i])
		dataCalc['ACID_TEST'][i] = Calcs.Solvency.acidTest(data['CASH_EQ_STI'][i], data['ACCTS_REC'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['QUICK_RATIO'][i] = Calcs.Solvency.quickRatio(data['TOTAL_CURR_ASSETS'][i], data['INV'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['QUICK_RATIO_2'][i] = Calcs.Solvency.quickRatio2(data['TOTAL_CURR_ASSETS'][i], data['INV'][i], data['PREPAID_EXP'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['CURRENT_RATIO'][i] = Calcs.Solvency.currentRatio(data['TOTAL_CURR_ASSETS'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['WORKING_CAP_RATIO'][i] = Calcs.Solvency.workingCapitalRatio(data['TOTAL_CURR_ASSETS'][i], data['TOTAL_CURR_LIAB'][i], data['TOTAL_ASSETS1'][i])
		# Capital Structure:		
		dataCalc['EQUITY_RATIO'][i] = Calcs.CapStructure.equityRatio(data['TOTAL_EQUITY'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i] = Calcs.CapStructure.equityMultiplier1(data['TOTAL_ASSETS1'][i], data['TOTAL_EQUITY'][i])
		# Asset Activity:
		dataCalc['SALES_TURNOVER'][i] = Calcs.Asset_Activity.salesTurnover(data['ACCTS_REC'][i], data['CREDIT_SALES'][i])
		dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i] = Calcs.Asset_Activity.receivablesTurnover(data['ACCTS_REC'][i], data['REV'][i])
		# Liability Activity:
		dataCalc['PAYABLES_TURNOVER_COGS'][i] = Calcs.Liab_Activity.payablesTurnoverCOGS(data['PAYABLES'][i], data['COGS'][i])
		dataCalc['PAYABLES_TURNOVER_COS'][i] = Calcs.Liab_Activity.payablesTurnoverCOS(data['PAYABLES'][i], data['COST_OF_REV'][i])
		dataCalc['CHG_DEBT_REPAYMENT_REQ'][i] = Calcs.Liab_Activity.changeStDebt(data['ST_DEBT'][i], data['ST_DEBT'][i+1])
		# Profitability:
		dataCalc['ROS'][i] = Calcs.Profitability.returnOnSales(data['NI_INC'][i], data['REV'][i])
		dataCalc['ROE'][i] = Calcs.Profitability.returnOnEquity(data['NI_INC'][i], data['TOTAL_EQUITY'][i])
		dataCalc['ROA'][i] = Calcs.Profitability.returnOnAssets(data['NI_INC'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['EPS_DILUTED_NI'][i] = Calcs.Profitability.earningsPerShare(data['NI_INC'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['EPS_DILUTED_EBIT'][i] = Calcs.Profitability.earningsPerShare(dataCalc['EBIT'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		dataCalc['ROCE_NI'][i] = Calcs.Profitability.returnOnCapitalEmployedNI(data['NI_INC'][i], data['TOTAL_ASSETS1'][i], data['TOTAL_CURR_LIAB'][i])
		dataCalc['GROSS_MARGIN'][i] = Calcs.Profitability.grossMarginRatio(data['PROFIT'][i], data['REV'][i])
		dataCalc['NOPAT_NI'][i] = Calcs.Profitability.netOperatingProfitAfterTaxNI(data['NI_INC'][i], data['NON_OP_INC_LOSS'][i], data['INT_EXP'][i])
		dataCalc['OPERATING_RATIO'][i] = Calcs.Profitability.operatingRatio(data['OP_EXP'][i], data['REV'][i])
		dataCalc['OP_PROFIT_MARGIN'][i] = Calcs.Profitability.operatingProfitMargin(data['OP_INC_LOSS'][i], data['REV'][i])
		# Dividends:
		dataCalc['RETENTION_RATIO'][i] = Calcs.Dividends.retentionRatio(data['RE'][i], data['NI_INC'][i])
		dataCalc['DIV_PAYOUT_RATIO'][i] = Calcs.Dividends.dividendPayoutRatio(data['DIVS_PAID'][i], data['NI_INC'][i])
		
		i += 1

	i = 1
	# Compute Intermediate Averages:
	dataCalc['AVG_NI_3YEAR'] = [None] * 35
	dataCalc['AVG_EBIT_3YEAR'] = [None] * 35
	dataCalc['AVG_LEV_FCF_3YEAR'] = [None] * 35
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break
		#Write recursive average Functions
		dataCalc['AVG_NI_3YEAR'][i] = round(Calcs.Basics.threeYearAvg(data['NI_INC'][i], data['NI_INC'][i+1], data['NI_INC'][i+1]), 2) if (Calcs.Basics.threeYearAvg(data['NI_INC'][i], data['NI_INC'][i+1], data['NI_INC'][i+1]) != None) else None
		dataCalc['AVG_EBIT_3YEAR'][i] = round(Calcs.Basics.threeYearAvg(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], dataCalc['EBIT'][i+1]), 2) if (Calcs.Basics.threeYearAvg(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], dataCalc['EBIT'][i+1]) != None) else None
		dataCalc['AVG_LEV_FCF_3YEAR'][i] = Calcs.Basics.threeYearAvg(dataCalc['LEV_FCF'][i], dataCalc['LEV_FCF'][i+1], dataCalc['LEV_FCF'][i+1])
		dataCalc['AVG_WORKING_CAPITAL'][i] = Calcs.Basics.avg(dataCalc['WORKING_CAPITAL'][i], dataCalc['WORKING_CAPITAL'][i+1])
		dataCalc['AVG_INVEST'][i] = Calcs.Basics.avg(dataCalc['TOTAL_INVEST'][i], dataCalc['TOTAL_INVEST'][i+1])
		dataCalc['AVG_DEBT'][i] = Calcs.Basics.avg(dataCalc['TOTAL_DEBT'][i], dataCalc['TOTAL_DEBT'][i+1])
		dataCalc['EBITDA_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EBITDA'][i], dataCalc['EBITDA'][i+1]))
		dataCalc['EBIT_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1]))
		dataCalc['EPS_GROWTH_RATE'][i] = Calcs.Display.GrowthRate(Calcs.Basics.growthRate(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1]))
	
		i += 1

	i = 1
	# Dependent calculations:
	while(i < 34):
		#Stop if error:
		if(dataCalc['YEAR_INC'][i] != dataCalc['YEAR_BAL'][i] and dataCalc['YEAR_CF'][i] != dataCalc['YEAR_BAL'][i]):
			print("Year mismatch error: ", dataCalc['YEAR_INC'][i], dataCalc['YEAR_BAL'][i], dataCalc['YEAR_CF'][i])
			break

		# Basic Functions
		dataCalc['LEV_FCF'][i] = Calcs.Basics.leveredFreeCashFlow(data['NI_INC'][i], data['DEPRE_AMORT'][i], dataCalc['WORKING_CAPITAL'][i], dataCalc['WORKING_CAPITAL'][i+1], dataCalc['CAPEX'][i])
		dataCalc['UN_LEV_FCF'][i] = Calcs.Basics.unleveredFreeCashFlow(data['NI_INC'][i], data['NON_CASH_ITEMS'][i], dataCalc['WORKING_CAPITAL'][i], dataCalc['WORKING_CAPITAL'][i+1], dataCalc['CAPEX'][i])
		# Solvency:
		dataCalc['INT_SERVICE_RATIO'][i] = Calcs.Solvency.interestServiceRatio(dataCalc['EBIT'][i], data['INT_EXP'][i])
		dataCalc['DEBT_SERVICE_RATIO'][i] = Calcs.Solvency.debtServiceCoverageRatio(dataCalc['EBIT'][i], data['INT_EXP'][i], data['ST_DEBT'][i])
		# Capital Structure:
		dataCalc['NET_DEBT'][i] = Calcs.CapStructure.netDebt(dataCalc['TOTAL_DEBT'][i], data['CASH_EQ'][i])
		dataCalc['DEBT_RATIO'][i] = Calcs.CapStructure.debtRatio(dataCalc['TOTAL_DEBT'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['DEBT_EQ_RATIO'][i] = Calcs.CapStructure.debtEquityRatio(dataCalc['TOTAL_DEBT'][i], data['TOTAL_EQUITY'][i])
		dataCalc['DEBT_TO_NI'][i] = Calcs.CapStructure.debtIncomeRatio(dataCalc['TOTAL_DEBT'][i], data['NI_INC'][i])
		dataCalc['FIXED_CHARGE_COVERAGE'][i] = Calcs.CapStructure.fixedChargeCoverage(dataCalc['EBIT'][i], data['CHG_FIXED_INTANG'][i], data['INT_EXP'][i])
		dataCalc['DEGREE_COMBINED_LEV'][i] = Calcs.CapStructure.degreeCombinedLeverage(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1], data['REV'][i], data['REV'][i+1])
		dataCalc['DEGREE_OPERATING_LEV'][i] = Calcs.CapStructure.degreeOperatingLeverage(dataCalc['EBIT'][i], dataCalc['EBIT'][i+1], data['REV'][i], data['REV'][i+1])
		dataCalc['DEGREE_FINANCIAL_LEV'][i] = Calcs.CapStructure.degreeFinancialLeverage(dataCalc['EPS_DILUTED_NI'][i], dataCalc['EPS_DILUTED_NI'][i+1], dataCalc['EBIT'][i], dataCalc['EBIT'][i+1])
		dataCalc['DFL_RATIO'][i] = Calcs.CapStructure.dflRatio(dataCalc['EBIT'][i], data['INT_EXP'][i])
		dataCalc['FINANCIAL_LEVERAGE'][i] = Calcs.CapStructure.financialLeverage(dataCalc['AVG_ASSETS'][i], dataCalc['AVG_EQUITY'][i])
		dataCalc['EQUITY_MULTIPLIER_RATIO_2'][i] = Calcs.CapStructure.equityMultiplier2(dataCalc['DEBT_RATIO'][i])
		dataCalc['NAV'][i] = Calcs.CapStructure.netAssetValue(data['TOTAL_ASSETS1'][i], data['TOTAL_LIAB'][i], dataCalc['EPS_DILUTED_NI'][i])
		dataCalc['EFFECTIVE_INT_RATE'][i] = Calcs.CapStructure.effectiveInterestRate(data['INT_EXP'][i], dataCalc['TOTAL_DEBT'][i])
		dataCalc['DEBT_COST_CAP'][i] = Calcs.CapStructure.debtCostCapital(dataCalc['EFFECTIVE_INT_RATE'][i], dataCalc['MARGINAL_TAX_RATE'][i])
		dataCalc['WACC'][i] = Calcs.CapStructure.wacc(data['TOTAL_EQUITY'][i], dataCalc['TOTAL_DEBT'][i], dataCalc['FAIR_RETURN_RATE'][i], dataCalc['EFFECTIVE_INT_RATE'][i], dataCalc['MARGINAL_TAX_RATE'][i])
		# Asset Activity:
		dataCalc['DSO'][i] = Calcs.Asset_Activity.daysSalesOutstanding(dataCalc['SALES_TURNOVER'][i])
		dataCalc['ASSET_TURNOVER'][i] = Calcs.Asset_Activity.assetTurnover(data['REV'][i], dataCalc['AVG_ASSETS'][i])
		dataCalc['ASSET_TURN_RATE'][i] = Calcs.Asset_Activity.assetTurnoverRate(dataCalc['ASSET_TURNOVER'][i])
		dataCalc['LT_ASSET_TURNOVER'][i] = Calcs.Asset_Activity.longTermAssetTurnover(data['REV'][i], dataCalc['AVG_LT_ASSETS'][i])
		dataCalc['LT_ASSET_TURN_RATE'][i] = Calcs.Asset_Activity.longTermAssetTurnoverRate(dataCalc['LT_ASSET_TURNOVER'][i])
		dataCalc['INV_SALES_TURNOVER'][i] = Calcs.Asset_Activity.inventorySalesTurnover(data['REV'][i], dataCalc['AVG_INVENTORY'][i])
		dataCalc['DSI'][i] = Calcs.Asset_Activity.daysSalesInventory(dataCalc['INV_SALES_TURNOVER'][i])
		dataCalc['INV_COGS_TURNOVER'][i] = Calcs.Asset_Activity.inventoryCOGSTurnover(data['COGS'][i], dataCalc['AVG_INVENTORY'][i])
		dataCalc['DIO'][i] = Calcs.Asset_Activity.daysInventoryOutstanding(dataCalc['INV_COGS_TURNOVER'][i])
		dataCalc['DRO'][i] = Calcs.Asset_Activity.daysReceivablesOutstanding(dataCalc['RECEIVABLES_ACCTS_TURNOVER'][i])
		dataCalc['WORKING_CAP_TURNOVER'][i] = Calcs.Asset_Activity.workingCapitalTurnover(data['REV'][i], dataCalc['AVG_WORKING_CAPITAL'][i])
		dataCalc['DWC'][i] = Calcs.Asset_Activity.daysWorkingCapital(dataCalc['WORKING_CAP_TURNOVER'][i])
		dataCalc['ROI_INVESTMENTS'][i] = Calcs.Asset_Activity.investmentsROI(data['CASH_INVEST_ACT1'][i], dataCalc['AVG_INVEST'][i])
		# Liability Activity:
		dataCalc['CREDITORS_TURNOVER'][i] = Calcs.Liab_Activity.CreditorsTurnover(data['CREDIT_SALES'][i], dataCalc['AVG_RECEIVABLES'][i])
		dataCalc['CDO'][i] = Calcs.Liab_Activity.CreditorsDaysOutstanding(dataCalc['CREDITORS_TURNOVER'][i])
		dataCalc['LIAB_TURNOVER'][i] = Calcs.Liab_Activity.liabitiesTurnover(data['TOTAL_LIAB'][i], dataCalc['AVG_PAYABLES_ACCRUALS'][i])
		dataCalc['DPO_COGS'][i] = Calcs.Liab_Activity.daysPayableOutstandingCOGS(dataCalc['PAYABLES_TURNOVER_COGS'][i])
		dataCalc['LIAB_TURN_RATE'][i] = Calcs.Liab_Activity.liabitiesTurnoverRate(dataCalc['LIAB_TURNOVER'][i])
		dataCalc['DPO_COS'][i] = Calcs.Liab_Activity.daysPayableOutstandingCOS(dataCalc['PAYABLES_TURNOVER_COS'][i])
		dataCalc['DEBTORS_PAYBACK_PERIOD'][i] = Calcs.Liab_Activity.debtorsPaybackPeriod(dataCalc['AVG_DEBT'][i], data['CASH_REPAY_DEBT'][i])
		dataCalc['BURN_RATE'][i] = Calcs.Liab_Activity.burnRate(data['CASH_EQ'][i], dataCalc['EBIT'][i])
		# Profitability
		dataCalc['CCC'][i] = Calcs.Profitability.cashConversionCycle(dataCalc['DIO'][i], dataCalc['DSO'][i], dataCalc['DPO_COGS'][i])
		dataCalc['ROCE_EBIT'][i] = Calcs.Profitability.returnOnCapitalEmployedEBIT(dataCalc['EBIT'][i], data['TOTAL_ASSETS1'][i], data['TOTAL_CURR_LIAB'][i])
		#dataCalc['PE'][i] = Calcs.Profitability.priceEarnings(data['PRICE'][i], data['DIL_WEIGHT_AVG_SHARES'][i], dataCalc['NI_INC'][i])
		#dataCalc['PE_REL_3'][i] = Calcs.Profitability.priceEarnings3(dataCalc['PE'][i], dataCalc['PE'][i+1], dataCalc['PE'][i+2])
		#dataCalc['PE_REL_5'][i] = Calcs.Profitability.priceEarnings5(dataCalc['PE'][i], dataCalc['PE'][i+1], dataCalc['PE'][i+2], dataCalc['PE'][i+3], dataCalc['PE'][i+4])
		dataCalc['EARNINGS_POWER'][i] = Calcs.Profitability.earningsPower(dataCalc['EBIT'][i], data['TOTAL_ASSETS1'][i])
		dataCalc['ROIC'][i] = Calcs.Profitability.returnOnInvestedCapital(dataCalc['NOPAT_NI'][i], dataCalc['TOTAL_INVEST'][i])
		dataCalc['NOPAT_EBIT'][i] = Calcs.Profitability.netOperatingProfitAfterTaxEBIT(data['OP_INC_LOSS'][i], dataCalc['MARGINAL_TAX_RATE'][i])
		# Valuation Measures:
		#dataCalc['MV'][i] = Calcs.Valuations.marketCap(data['PRICE'][i], data['DIL_WEIGHT_AVG_SHARES'][i])
		#dataCalc['MV_EBIT_RATIO'][i] = Calcs.Valuations.marketCapEBITRatio(dataCalc['MV'][i], dataCalc['EBIT'][i])
		dataCalc['ORIG_GRAHAM'][i] = Calcs.Valuations.originalGraham(dataCalc['EPS_DILUTED_NI'][i], dataCalc['NO_GROWTH_PE'][i], dataCalc['GROWTH_MULTIPLE'][i], dataCalc['EPS_GROWTH_RATE'][i])
		dataCalc['REVISED_GRAHAM'][i] = Calcs.Valuations.revisedGraham(dataCalc['EPS_DILUTED_NI'][i], dataCalc['NO_GROWTH_PE'][i], dataCalc['GROWTH_MULTIPLE'][i], dataCalc['EPS_GROWTH_RATE'][i], dataCalc['REQUIRED_RETURN'][i], dataCalc['AAA_BOND_YIELD'][i])
		#dataCalc['EV'][i] = Calcs.Valuations.enterpriseValue(dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ'][i])
		#dataCalc['EV_EBIT'][i] = Calcs.Valuations.enterpriseValueEBIT(dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ'][i], dataCalc['EBIT'][i])
		#dataCalc['EV_NI'][i] = Calcs.Valuations.enterpriseValueNI(dataCalc['MV'][i], dataCalc['TOTAL_DEBT'][i], data['CASH_EQ'][i], data['NI_INC'][i])
		dataCalc['BV'][i] = Calcs.Valuations.bookValue(data['TOTAL_ASSETS1'][i], data['TOTAL_INTANG_ASSETS'][i], data['TOTAL_LIAB'][i+1])
		dataCalc['BV_NI'][i] = Calcs.Valuations.bookValueNIperShare(dataCalc['BV'][i], dataCalc['EPS_DILUTED_NI'][i])
		dataCalc['BV_EBIT'][i] = Calcs.Valuations.bookValueEBITperShare(dataCalc['BV'][i], dataCalc['EPS_DILUTED_EBIT'][i])
		#dataCalc['PRICE_SALES'][i] = Calcs.Valuations.priceToSales(dataCalc['PRICE'][i], data['REV'][i])
		#dataCalc['PRICE_BOOK'][i] = Calcs.Valuations.priceToBook(dataCalc['PRICE'][i], dataCalc['BV'][i])
		#dataCalc['PRICE_NAV'][i] = Calcs.Valuations.priceToNAV(dataCalc['PRICE'][i], dataCalc['NAV'][i])
		#dataCalc['PRICE_FCF'][i] = Calcs.Valuations.pricetoLeveredFreeCashFlow(dataCalc['PRICE'][i], dataCalc['LEV_FCF'][i])
		#dataCalc['PRICE_UN_FCF'][i] = Calcs.Valuations.priceToUnLeveredFreeCashFlow(dataCalc['PRICE'][i], dataCalc['UN_LEV_FCF'][i])
		#dataCalc['MV_OCF'][i] = Calcs.Valuations.marketValueToOCF(dataCalc['MV'][i], dataCalc['EBIT'][i])
		#dataCalc['CASH_PRICE_RATIO'][i] = Calcs.Valuations.cashPriceRatio(dataCalc['MV'][i], data['CASH_EQ'][i])
		dataCalc['INTRINSIC_VALUE_NI'][i] = Calcs.Valuations.intrinsicValueNI(0, dataCalc['AVG_NI_3YEAR'][i], dataCalc['FAIR_RETURN_RATE'][i], 1)
		dataCalc['INTRINSIC_VALUE_EBIT'][i] = Calcs.Valuations.intrinsicValueEBIT(0, dataCalc['AVG_EBIT_3YEAR'][i], dataCalc['FAIR_RETURN_RATE'][i], 1)
		dataCalc['INTRINSIC_VALUE_FCF'][i] = Calcs.Valuations.intrinsicValueFCF(0, dataCalc['AVG_LEV_FCF_3YEAR'][i], dataCalc['FAIR_RETURN_RATE'][i], 1)
		#dataCalc['MARGIN_OF_SAFETY_NI'][i] = Calcs.Valuations.marginOfSafety_NI(dataCalc['INTRINSIC_VALUE_NI'][i], dataCalc['MV'][i])
		#dataCalc['MARGIN_OF_SAFETY_EBIT'][i] = Calcs.Valuations.marginOfSafety_EBIT(dataCalc['INTRINSIC_VALUE_EBIT'][i], dataCalc['MV'][i])
		#dataCalc['MARGIN_OF_SAFETY_FCF'][i] = Calcs.Valuations.marginOfSafety_FCF(dataCalc['INTRINSIC_VALUE_FCF'][i], dataCalc['MV'][i])
		dataCalc['DUPONT_SYSTEM_1'][i] = Calcs.Valuations.dupontSystem_1(dataCalc['ROS'][i], dataCalc['ASSET_TURNOVER'][i], dataCalc['EQUITY_MULTIPLIER_RATIO_1'][i])
		dataCalc['DUPONT_SYSTEM_2'][i] = Calcs.Valuations.dupontSystem_2(dataCalc['ROA'][i], dataCalc['DEBT_EQ_RATIO'][i])
		# Dividends: 
		dataCalc['EARNINGS_YIELD'][i] = Calcs.Dividends.earningsYieldRatio(data['NI_INC'][i], dataCalc['MV'][i])
		dataCalc['DIVS_YIELD'][i] = Calcs.Dividends.dividendYieldRatio(data['DIVS_PAID'][i], dataCalc['MV'][i])
		dataCalc['SGR'][i] = Calcs.Dividends.sustainableGrowthRate(dataCalc['ROE'][i], dataCalc['DIV_PAYOUT_RATIO'][i])
		
		i += 1
		
	print(dataCalc)
	filename = dataCalc['symbol']
	ToFile(path, filename, dataCalc)
	decorateFile(path, filename + ".json" )
	getTickerObject()

	return dataCalc








	# Basic Functions:
	#print(dataCalc['REV_GROWTH_RATE'])
	#print(dataCalc['EBITDA_GROWTH_RATE'])
	#print(dataCalc['EBIT_GROWTH_RATE'])
	#print(dataCalc['NI_GROWTH_RATE'])
	#print(dataCalc['EPS_GROWTH_RATE'])
	#print(dataCalc['LEV_FCF'])
	#print(dataCalc['UN_LEV_FCF'])
	#print(dataCalc['COST_OF_SALES'])
	#print(dataCalc['WORKING_CAPITAL'])
	#print(dataCalc['CAPITAL_EMPLOYED'])
	#print(dataCalc['TOTAL_INVEST'])
	#print(dataCalc['TOTAL_DEBT'])
	#print(dataCalc['EBIT'])
	#print(dataCalc['EBIAT'])
	#print(dataCalc['EBITDA'])
	#print(dataCalc['CAPEX'])
	#print(dataCalc['EPS_DILUTED_NI'])
	# Averages:
	#print(dataCalc['AVG_RECEIVABLES'])
	#print(dataCalc['AVG_PAYABLES_ACCRUALS'])
	#print(dataCalc['AVG_INVENTORY'])
	#print(dataCalc['AVG_LT_ASSETS'])
	#print(dataCalc['AVG_ASSETS'])
	#print(dataCalc['AVG_LIABILITIES'])
	#print(dataCalc['AVG_EQUITY'])
	#print(dataCalc['AVG_WORKING_CAPITAL'])
	#print(dataCalc['AVG_INVEST'])
	#print(dataCalc['AVG_DEBT'])
	# Solvency:
	#print(dataCalc['CASH_RATIO'])
	#print(dataCalc['CASH_SERVICE_RATIO'])
	#print(dataCalc['CASH_COVERAGE_RATIO'])
	#print(dataCalc['ACID_TEST'])
	#print(dataCalc['QUICK_RATIO'])
	#print(dataCalc['QUICK_RATIO_2'])
	#print(dataCalc['CURRENT_RATIO'])
	#print(dataCalc['WORKING_CAP_RATIO'])
	#print(dataCalc['INT_SERVICE_RATIO'])
	#print(dataCalc['DEBT_SERVICE_RATIO'])
	# Capital Structure:
	#print(dataCalc['EQUITY_RATIO'])
	#print(dataCalc['EQUITY_MULTIPLIER_RATIO_1'])
	#print(dataCalc['NET_DEBT'])
	#print(dataCalc['DEBT_RATIO'])
	#print(dataCalc['DEBT_EQ_RATIO'])
	#print(dataCalc['DEBT_TO_NI'])
	#print(dataCalc['FIXED_CHARGE_COVERAGE'])
	#print(dataCalc['DEGREE_COMBINED_LEV'])
	#print(dataCalc['DEGREE_OPERATING_LEV'])
	#print(dataCalc['DEGREE_FINANCIAL_LEV'])
	#print(dataCalc['DFL_RATIO'])
	#print(dataCalc['FINANCIAL_LEVERAGE'])
	#print(dataCalc['EQUITY_MULTIPLIER_RATIO_2'])
	#print(dataCalc['NAV'])
	#print(dataCalc['EFFECTIVE_INT_RATE'])
	#print(dataCalc['DEBT_COST_CAP'])
	#print(dataCalc['WACC'])
	# Asset Activity:
	#print(dataCalc['SALES_TURNOVER'])
	#print(dataCalc['RECEIVABLES_ACCTS_TURNOVER'])
	#print(dataCalc['DSO'])
	#print(dataCalc['ASSET_TURNOVER'])
	#print(dataCalc['ASSET_TURN_RATE'])
	#print(dataCalc['LT_ASSET_TURNOVER'])
	#print(dataCalc['LT_ASSET_TURN_RATE'])
	#print(dataCalc['INV_SALES_TURNOVER'])
	#print(dataCalc['DSI'])
	#print(dataCalc['INV_COGS_TURNOVER'])
	#print(dataCalc['DIO'])
	#print(dataCalc['DRO'])
	#print(dataCalc['WORKING_CAP_TURNOVER'])
	#print(dataCalc['DWC'])
	#print(dataCalc['ROI_INVESTMENTS'])
	# Liability Activity
	#print(dataCalc['CREDITORS_TURNOVER'])
	#print(dataCalc['CDO'])
	#print(dataCalc['PAYABLES_TURNOVER_COGS'])
	#print(dataCalc['DPO_COGS'])
	#print(dataCalc['PAYABLES_TURNOVER_COS'])
	#print(dataCalc['DPO_COGS'])
	#print(dataCalc['LIAB_TURNOVER'])
	#print(dataCalc['LIAB_TURN_RATE'])
	#print(dataCalc['CHG_DEBT_REPAYMENT_REQ'])
	#print(dataCalc['DEBTORS_PAYBACK_PERIOD'])
	#print(dataCalc['BURN_RATE'])
	# Profitability:
	#print(dataCalc['CCC'])
	#print(dataCalc['ROCE_EBIT'])
	#print(dataCalc['EARNINGS_POWER'])
	#print(dataCalc['ROIC'])
	#print(dataCalc['NOPAT_EBIT'])
	#print(dataCalc['PE'])
	#print(dataCalc['PE_REL_3'])
	#print(dataCalc['PE_REL_5'])
	#print(dataCalc['EBITDA_GROWTH_RATE'])
	#print(dataCalc['EBIT_GROWTH_RATE'])
	#print(dataCalc['EPS_GROWTH_RATE'])
	#print(dataCalc['ROS'])
	#print(dataCalc['ROE'])
	#print(dataCalc['ROA'])
	#print(dataCalc['EPS_DILUTED_NI'])
	#print(dataCalc['ROCE_NI'])
	#print(dataCalc['GROSS_MARGIN'])
	#print(dataCalc['NOPAT_NI'])
	#print(dataCalc['OPERATING_RATIO'])
	#print(dataCalc['OP_PROFIT_MARGIN'])
	# Valuation Measures:
	#print(dataCalc['MV'])
	#print(dataCalc['MV_EBIT_RATIO'])
	#print(dataCalc['ORIG_GRAHAM'])
	#print(dataCalc['REVISED_GRAHAM'])
	#print(dataCalc['EV'])
	#print(dataCalc['EV_EBIT'])
	#print(dataCalc['EV_NI'])
	#print(dataCalc['BV'])
	#print(dataCalc['BV_NI'])
	#print(dataCalc['BV_EBIT'])
	#print(dataCalc['PRICE_SALES'])
	#print(dataCalc['PRICE_BOOK']) 
	#print(dataCalc['PRICE_NAV'])
	#print(dataCalc['PRICE_FCF'])
	#print(dataCalc['PRICE_UN_FCF'])
	#print(dataCalc['MV_OCF'])
	#print(dataCalc['CASH_PRICE_RATIO'])
	#print(dataCalc['INTRINSIC_VALUE_NI'])
	#print(dataCalc['INTRINSIC_VALUE_EBIT'])
	#print(dataCalc['INTRINSIC_VALUE_FCF'])
	#print(dataCalc['MARGIN_OF_SAFETY_NI'])
	#print(dataCalc['MARGIN_OF_SAFETY_EBIT'])
	#print(dataCalc['MARGIN_OF_SAFETY_FCF'])
	#print(dataCalc['DUPONT_SYSTEM_1'])
	#print(dataCalc['DUPONT_SYSTEM_2'])
	# Dividends:
	#print(dataCalc['RETENTION_RATIO'])
	#print(dataCalc['DIV_PAYOUT_RATIO'])
	#print(dataCalc['EARNINGS_YIELD'])
	#print(dataCalc['DIVS_YIELD'])
	#print(dataCalc['SGR'])		



#*************************************************
#Recursive Function Design
#*************************************************

#def recurse(i):
#	print(i)
#	return i if (i > 10) else recurse(i+1)
	

#value = recurse(i)

#print("i finished at:" + str(value))
#DISC_RATE = 0.15
#NI_3YEAR_AVG = 100
#value = 0
#i = 1

def intrinsicValueNI(value, NI_3YEAR_AVG, DISC_RATE, i):
	#print(str((i-1)) + ": " + str(value))
	value = (value + (NI_3YEAR_AVG / ((1 + DISC_RATE) ** i)) )
	return value if (NI_3YEAR_AVG / ((1 + DISC_RATE) ** i) < 1) else intrinsicValueNI(value, NI_3YEAR_AVG, DISC_RATE, i+1)

#iValue = intrinsicValueNI(value, NI_3YEAR_AVG, DISC_RATE, i)
#print("iValue: " + str(iValue))

## Basics
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
#dataCalc['CASH_RATIO']
#dataCalc['CASH_SERVICE_RATIO']
#dataCalc['INT_SERVICE_RATIO']
#dataCalc['CASH_COVERAGE_RATIO']
#dataCalc['ACID_TEST']
#dataCalc['QUICK_RATIO']
#dataCalc['QUICK_RATIO_2']
#dataCalc['CURRENT_RATIO']
#dataCalc['WORKING_CAP_RATIO']
#dataCalc['DEBT_SERVICE_RATIO']
#dataCalc['NET_DEBT']
#dataCalc['DEBT_RATIO']
#dataCalc['DEBT_EQ_RATIO']
#dataCalc['DEBT_TO_NI']
#dataCalc['FIXED_CHARGE_COVERAGE']
#dataCalc['DEGREE_COMBINED_LEV']
#dataCalc['DEGREE_OPERATING_LEV']
#dataCalc['DEGREE_FINANCIAL_LEV']
#dataCalc['DFL_RATIO']
#dataCalc['FINANCIAL_LEVERAGE']
#dataCalc['EQUITY_RATIO']
#dataCalc['EQUITY_MULTIPLIER_RATIO_1']
#dataCalc['EQUITY_MULTIPLIER_RATIO_2']
#dataCalc['NAV']
#dataCalc['DEBT_COST_CAP']
#dataCalc['EFFECTIVE_INT_RATE']
#dataCalc['FAIR_RETURN_RATE']
#dataCalc['WACC']
#dataCalc['SALES_TURNOVER']
#dataCalc['DSO']
#dataCalc['ASSET_TURNOVER']
#dataCalc['ASSET_TURN_RATE']
#dataCalc['FIXED_ASSET_TURNOVER']
#dataCalc['FIXED_ASSET_TURN_RATE']
#dataCalc['INV_SALES_TURNOVER']
#dataCalc['DSI']
#dataCalc['INV_COGS_TURNOVER']
#dataCalc['DIO']
#dataCalc['RECEIVABLES_ACCTS_TURNOVER']
#dataCalc['DRO']
#dataCalc['WORKING_CAP_TURNOVER']
#dataCalc['DWC']
#dataCalc['CCC']
#dataCalc['ROI_INVESTMENTS']
#datacalc['creditors_turnover']
#datacalc['cdo']
#datacalc['payables_turnover_cogs']
#datacalc['dpo_cogs']
#datacalc['payables_turnover_cos']
#datacalc['dpo_cos']
#datacalc['liab_turnover']
#datacalc['liab_turn_rate']
#datacalc['chg_debt_repayment_req']
#datacalc['debtors_payback_period']
#datacalc['burn_rate']
#dataCalc['ROS']
#dataCalc['ROE']
#dataCalc['ROA']
#dataCalc['ROCE_NI']
#dataCalc['EPS']
#dataCalc['EPS_DILUTED_NI']
#dataCalc['ROCE_EBIT']
#dataCalc['PE']
#dataCalc['PE_REL_3']
#dataCalc['PE_REL_5']
#dataCalc['EARNINGS_POWER']
#dataCalc['GROSS_MARGIN']
#dataCalc['NOPAT_NI']
#dataCalc['NOPAT_EBIT']
#dataCalc['ROIC']
#dataCalc['OPERATING_RATIO']
#dataCalc['OP_PROFIT_MARGIN']
#dataCalc['MV']
#dataCalc['MV_EBIT_RATIO']
#dataCalc['ORIG_GRAHAM']
#dataCalc['REVISED_GRAHAM']
#dataCalc['EV']
#dataCalc['EV_EBIT']
#dataCalc['EV_NI']
#dataCalc['BV']
#dataCalc['BV_PER_SHARE']
#dataCalc['BV_NI']
#dataCalc['BV_EBIT']
#dataCalc['PRICE_SALES']
#dataCalc['PRICE_BOOK']
#dataCalc['PRICE_NAV']
#dataCalc['PRICE_FCF']
#dataCalc['PRICE_UN_FCF']
#dataCalc['MV_OCF']
#dataCalc['CASH_PRICE_RATIO']
#dataCalc['INTRINSIC_VALUE_NI']
#dataCalc['INTRINSIC_VALUE_EBIT']
#dataCalc['INTRINSIC_VALUE_UNFCF']
#dataCalc['INTRINSIC_VALUE_FCF']
#dataCalc['MARGIN_OF_SAFETY_NI']
#dataCalc['MARGIN_OF_SAFETY_EBIT']
#dataCalc['MARGIN_OF_SAFETY_UNFCF']
#dataCalc['MARGIN_OF_SAFETY_FCF']
#dataCalc['DUPONT_SYSTEM_1']
#dataCalc['DUPONT_SYSTEM_2']
#dataCalc['RETENTION_RATIO']
#dataCalc['DIV_PAYOUT_RATIO']
#dataCalc['EARNINGS_YIELD']
#dataCalc['DIVS_YIELD']
#dataCalc['SGR']							

#data['YEAR_INC']				
#data['REV']						
#data['SALES_SERV_REV']			
#data['OTHER_REV']				
#data['COST_OF_REV']				
#data['COGS']					
#data['PROFIT']					
#data['OTH_PROFIT']				
#data['OP_EXP']					
#data['SG_AND_ADMIN']			
#data['SELL_AND_MARK']			
#data['GEN_AND_ADMIN']			
#data['R_AND_D']					
#data['DEP_AMORT']				
#data['OTH_OP_EXP']				
#data['OP_INC_LOSS']				
#data['NON_OP_INC_LOSS']			
#data['NET_INT_EXP']				
#data['INT_EXP']				
#data['INT_INC']					
#data['FOREX']					
#data['AFFILIATES']				
#data['NON_OP_INC']				
#data['PRETAX_INCOME']			
#data['INC_TAX_BENEFIT']			
#data['CURR_INC_TAX']			
#data['DEFF_INC_TAX']			
#data['CONT_OPS']				
#data['NET_EXTRA1']				
#data['DISC_OPS']				
#data['ACCT_CHNG']				
#data['INCOME_MI']				
#data['MIN_INTEREST']			
#data['NI_INC']  				
#data['PREF_DIVS']				
#data['OTH_ADJ']					
#data['NI_AVAIL_COMMON_GAAP']	
#data['NI_AVAIL_COMMON_ADJ']		
#data['NET_ABNORMAL']			
#data['NET_EXTRA2']				
#data['BASIC_WEIGHT_AVG_SHARES'] 
#data['DIL_WEIGHT_AVG_SHARES']	
#data['YEAR_BAL']				
#data['TOTAL_ASSETS1']			
#data['CASH_EQ_STI']				
#data['CASH_EQ']					
#data['ST_INVEST']				
#data['ACCTS_REC']				
#data['ACCTS_REC_NET']			
#data['NOTES_REC_NET']			
#data['INV']						
#data['RAW_MAT']					
#data['WIP']						
#data['FIN_GOODS'] 				
#data['OTH_INV']					
#data['OTH_ST_ASSETS']			
#data['DERIV_HEDGE_ASSETS1']		
#data['TAXES_RECIEV']			
#data['MISC_ST_ASSETS']			
#data['TOTAL_CURR_ASSETS']		
#data['PPE_NET']					
#data['PPE']						
#data['ACC_DEPREC']				
#data['LTI_RECEIVABLES']			
#data['LT_INVEST']				
#data['OTH_LT_ASSETS']			
#data['TOTAL_INTANG_ASSETS']		
#data['GOODWILL']				
#data['OTH_INTANG_ASSETS']		
#data['PREPAID_EXP']				
#data['DEFF_TAX_ASSETS']			
#data['DERIV_HEDGE_ASSETS2']		
#data['MISC_ASSETS']				
#data['TOTAL_NON_CURR_ASSETS']	
#data['TOTAL_ASSETS2']			
#data['LIAB_AND_EQUITY1']		
#data['PAYABLES_ACCRUALS']		
#data['PAYABLES']				
#data['ACCRUED_TAXES']			
#data['INT_DIVS_PAYABLES']		
#data['OTH_PAYABLES_ACCURALS']	
#data['ST_DEBT']					
#data['ST_BORROWINGS']			
#data['ST_FIN_LEASES']			
#data['ST_OP_LEASES']			
#data['CURR_LT_DEBT']			
#data['OTH_ST_LIAB']				
#data['DEFF_REV_1']				
#data['DERIV_HEDGE_1']			
#data['MISC_ST_LIAB']			
#data['TOTAL_CURR_LIAB']			
#data['LT_DEBT']					
#data['LT_BORROW']				
#data['LT_FIN_LEASES']			
#data['LT_OP_LEASES']			
#data['OTH_LT_LIAB']				
#data['ACCURED_LIAB']			
#data['PENSION_LIAB']			
#data['PENSIONS']				
#data['OTH_POST_RET_BEN']		
#data['DEFF_REV_2']				
#data['DEF_TAX_LIAB']			
#data['DERIV_HEDGE_2']			
#data['MISC_LT_LIAB']			
#data['TOTAL_NON_CURR_LIAB']		
#data['TOTAL_LIAB']				
#data['PREF_EQUITY_HYBRID_CAP']	
#data['SHARE_CAP_APIC']			
#data['COMMON_STOCK']			
#data['ADD_PAID_CAP']			
#data['TREASURY_STOCK']			
#data['RE']						
#data['OTH_EQUITY']				
#data['EQUITY_BEFORE_MIN_INT']	
#data['MIN_NON_CONTROL_INT']		
#data['TOTAL_EQUITY']			
#data['LIAB_AND_EQUITY']			
#data['YEAR_CF']					
#data['NI_CF']  					
#data['DEPRE_AMORT']				
#data['NON_CASH_ITEMS']			
#data['STOCK_COMP']				
#data['DEF_INT_COMP']			
#data['OTH_NON_CASH_ADJ']		
#data['CHG_NON_CASH_OP']			
#data['CHG_ACCTS_REC']			
#data['CHG_INVENTORIES']			
#data['CHG_ACCTS_PAYABLE']		
#data['CHG_OTHER']				
#data['NET_CASH_DISC_OPS1']		
#data['CASH_OP_ACT']				
#data['CASH_INVEST_ACT1']		
#data['CHG_FIXED_INTANG']		
#data['DISP_FIXED_INTANG']		
#data['DISP_FIXED_PROD_ASSETS']	
#data['DISP_INTANG_ASSETS']		
#data['ACQ_FIXED_INTANG']		
#data['ACQ_FIXED_PROD_ASSETS']	
#data['ACQ_INTANG_ASSETS']		
#data['NET_CHG_LT_INVEST']		
#data['DEC_LT_INVEST']			
#data['INC_LT_INVEST']			
#data['NET_CASH_ACQ_DIV']		
#data['CASH_DIVEST']				
#data['CASH_ACQ_SUBS']			
#data['CASH_JVS']				
#data['OTH_INVEST_ACT']			
#data['NET_CASH_DISC_OPS2']		
#data['TOTAL_INVEST']		
#data['CASH_FIN_ACT1']			
#data['DIVS_PAID']				
#data['CASH_REPAY_DEBT']			
#data['CASH_ST_DEBT']			
#data['CASH_LT_DEBT']			
#data['REPAY_LT_DEBT']			
#data['CASH_REPURCH_EQUITY']		
#data['INC_CAPITAL_STOCK']		
#data['DEC_CAPITAL_STOCK']		
#data['OTH_FIN_ACT']				
#data['NET_CASH_DISC_OPS3']		
#data['CASH_FIN_ACT2']			
#data['EFFECT_FOREX_RATES']		
#data['NET_CHG_CASH']			
#data['CASH_PAID_TAXES']			
#data['CASH_PAID_INT']
