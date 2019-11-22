import sectors
import Enums
import instantiate
import json
import numpy as np
import Calcs

def organizeSectors(symbols):
	
	energyServices = []
	energyServices.append("Energy Services")
	materials = []
	materials.append("Materials")
	industrials = []
	industrials.append("Industrials")
	consumerDiscretionary = []
	consumerDiscretionary.append("Consumer Discretionary")
	consumerStaples = []
	consumerStaples.append("Consumer Staples")
	healthCare = []
	healthCare.append("Healthcare")
	financials = []
	financials.append("Financials")
	informationTechnology = []
	informationTechnology.append("Information Technology")
	utilities = []
	utilities.append("Utilities")
	realEstate = []
	realEstate.append("Real Estate")
	communicationServices = []
	communicationServices.append("Communication Services")

	i=0
	while(i < len(symbols)):
		if(sectors.div[symbols[i]] == Enums.Sector.ENRS):
			energyServices.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.MATR):
			materials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.INDU):
			industrials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.COND):
			consumerDiscretionary.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.CONS):
			consumerStaples.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.HLTH):
			healthCare.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.FINL):
			financials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.INFT):
			informationTechnology.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.UTIL):
			utilities.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.REAL):
			realEstate.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.TELS):
			communicationServices.append(symbols[i])
		i+=1

	sectorList = [energyServices, materials, industrials, consumerDiscretionary, consumerStaples, healthCare, financials, informationTechnology, utilities, realEstate, communicationServices]
	
	return sectorList


def makeSectorData(sectorList, dataList, dataCalcList):
	sec = 0
	sectors = []
	for sector in sectorList:
		sectorData = instantiate.instantiateSectors()
		for tick in range(len(sector)):
			sectorData['SECTOR'] = sectorList[sec][0]
			sectorData['LENGTH'] = len(sectorList[sec]) - 1

			if(1 < len(sectorList[sec]) and 0 < tick):
				#print(sectorList[sec][0], ": ", sectorList[sec][tick])
				idx =  dataCalcList.index(sectorList[sec][tick] + "Calc.json")
				#print(sectorList[sec][tick], ": ", sectorList[sec][0], dataCalcList.index(sectorList[sec][tick] + "Calc.json"))
				
				#print()
				#print()
				#print()
				#print(dataList[idx])
				#print(dataCalcList[idx])
				
				#Grab a ticker's json data & dataCalc file for appending to sector data
				#with open(dataList[tick]) as json_file:
				#	data = json.load(json_file)
				with open(dataCalcList[idx]) as json_file:
					dataCalc = json.load(json_file)
				#sectorData.append(dataCalc)

				year=1
				startYear = 2019
				while(year < 34):
					
					sectorData['YEAR_INC'][year] = startYear - year				
					sectorData['YEAR_BAL'][year] = startYear - year						
					sectorData['YEAR_CF'][year] = startYear - year
					sectorData['PRICE'][year].append(dataCalc['PRICE'][year])						
					sectorData['AVG_NI_3YEAR'][year].append(dataCalc['AVG_NI_3YEAR'][year])					
					sectorData['AVG_EBIT_3YEAR'][year].append(dataCalc['AVG_EBIT_3YEAR'][year])				
					sectorData['AVG_LEV_FCF_3YEAR'][year].append(dataCalc['AVG_LEV_FCF_3YEAR'][year])			
					sectorData['MARGINAL_TAX_RATE'][year].append(dataCalc['MARGINAL_TAX_RATE'][year])			
					sectorData['FAIR_RETURN_RATE'][year].append(dataCalc['FAIR_RETURN_RATE'][year])				
					sectorData['NO_GROWTH_PE'][year].append(dataCalc['NO_GROWTH_PE'][year])					
					sectorData['REQUIRED_RETURN'][year].append(dataCalc['REQUIRED_RETURN'][year])				
					sectorData['AAA_BOND_YIELD'][year].append(dataCalc['AAA_BOND_YIELD'][year])				
					sectorData['GROWTH_MULTIPLE'][year].append(dataCalc['GROWTH_MULTIPLE'][year])				
					sectorData['REV_GROWTH_RATE'][year].append(dataCalc['REV_GROWTH_RATE'][year])				
					sectorData['EBITDA_GROWTH_RATE'][year].append(dataCalc['EBITDA_GROWTH_RATE'][year])			
					sectorData['EBIT_GROWTH_RATE'][year].append(dataCalc['EBIT_GROWTH_RATE'][year])				
					sectorData['NI_GROWTH_RATE'][year].append(dataCalc['NI_GROWTH_RATE'][year])				
					sectorData['EPS_GROWTH_RATE'][year].append(dataCalc['EPS_GROWTH_RATE'][year])				
					sectorData['GROWTH_RATE'][year].append(dataCalc['GROWTH_RATE'][year]) 					
					sectorData['AVG_3YEARS'][year].append(dataCalc['AVG_3YEARS'][year]) 					
					sectorData['AVG_5YEARS'][year].append(dataCalc['AVG_5YEARS'][year]) 					
					sectorData['COST_OF_SALES'][year].append(dataCalc['COST_OF_SALES'][year])				
					sectorData['WORKING_CAPITAL'][year].append(dataCalc['WORKING_CAPITAL'][year]) 				
					sectorData['CAPITAL_EMPLOYED'][year].append(dataCalc['CAPITAL_EMPLOYED'][year])			
					sectorData['TOTAL_INVEST'][year].append(dataCalc['TOTAL_INVEST'][year])					
					sectorData['TOTAL_DEBT'][year].append(dataCalc['TOTAL_DEBT'][year])					
					sectorData['EBITDA'][year].append(dataCalc['EBITDA'][year])						
					sectorData['EBIAT'][year].append(dataCalc['EBIAT'][year])						
					sectorData['EBIT'][year].append(dataCalc['EBIT'][year])							
					sectorData['CAPEX'][year].append(dataCalc['CAPEX'][year]) 						
					sectorData['LEV_FCF'][year].append(dataCalc['LEV_FCF'][year])						
					sectorData['UN_LEV_FCF'][year].append(dataCalc['UN_LEV_FCF'][year])					
					sectorData['AVG_RECEIVABLES'][year].append(dataCalc['AVG_RECEIVABLES'][year]) 				
					sectorData['AVG_PAYABLES_ACCRUALS'][year].append(dataCalc['AVG_PAYABLES_ACCRUALS'][year]) 		
					sectorData['AVG_WORKING_CAPITAL'][year].append(dataCalc['AVG_WORKING_CAPITAL'][year]) 			
					sectorData['AVG_INVENTORY'][year].append(dataCalc['AVG_INVENTORY'][year])				
					sectorData['AVG_INVEST'][year].append(dataCalc['AVG_INVEST'][year]) 					
					sectorData['AVG_LT_ASSETS'][year].append(dataCalc['AVG_LT_ASSETS'][year]) 				
					sectorData['AVG_ASSETS'][year].append(dataCalc['AVG_ASSETS'][year]) 					
					sectorData['AVG_LIABILITIES'][year].append(dataCalc['AVG_LIABILITIES'][year])				
					sectorData['AVG_EQUITY'][year].append(dataCalc['AVG_EQUITY'][year]) 					
					sectorData['AVG_DEBT'][year].append(dataCalc['AVG_DEBT'][year]) 					
					sectorData['CASH_RATIO'][year].append(dataCalc['CASH_RATIO'][year])					
					sectorData['CASH_STI_RATIO'][year].append(dataCalc['CASH_STI_RATIO'][year])				
					sectorData['CASH_SERVICE_RATIO'][year].append(dataCalc['CASH_SERVICE_RATIO'][year])			
					sectorData['INT_SERVICE_RATIO'][year].append(dataCalc['INT_SERVICE_RATIO'][year])			
					sectorData['CASH_ST_DEBT_RATIO'][year].append(dataCalc['CASH_ST_DEBT_RATIO'][year]) 			
					sectorData['ACID_TEST'][year].append(dataCalc['ACID_TEST'][year])					
					sectorData['QUICK_RATIO'][year].append(dataCalc['QUICK_RATIO'][year])					
					sectorData['QUICK_RATIO_2'][year].append(dataCalc['QUICK_RATIO_2'][year])				
					sectorData['CURRENT_RATIO'][year].append(dataCalc['CURRENT_RATIO'][year])				
					sectorData['NWC_TO_TA'][year].append(dataCalc['NWC_TO_TA'][year])					
					sectorData['DEBT_SERVICE_RATIO'][year].append(dataCalc['DEBT_SERVICE_RATIO'][year]) 			
					sectorData['CHG_ST_DEBT'][year].append(dataCalc['CHG_ST_DEBT'][year])					
					sectorData['CHG_LT_DEBT'][year].append(dataCalc['CHG_LT_DEBT'][year])					
					sectorData['CHG_NET_DEBT'][year].append(dataCalc['CHG_NET_DEBT'][year])					
					sectorData['NET_DEBT'][year].append(dataCalc['NET_DEBT'][year]) 					
					sectorData['DEBT_RATIO'][year].append(dataCalc['DEBT_RATIO'][year]) 					
					sectorData['TOTAL_CURR_LIAB_RATIO'][year].append(dataCalc['TOTAL_CURR_LIAB_RATIO'][year]) 		
					sectorData['LT_DEBT_RATIO'][year].append(dataCalc['LT_DEBT_RATIO'][year]) 				
					sectorData['DEBT_EQ_RATIO'][year].append(dataCalc['DEBT_EQ_RATIO'][year]) 				
					sectorData['DEBT_TO_EBIT'][year].append(dataCalc['DEBT_TO_EBIT'][year]) 				
					sectorData['FIXED_CHARGE_COVERAGE'][year].append(dataCalc['FIXED_CHARGE_COVERAGE'][year]) 		
					sectorData['DEGREE_COMBINED_LEV'][year].append(dataCalc['DEGREE_COMBINED_LEV'][year]) 			
					sectorData['DEGREE_OPERATING_LEV'][year].append(dataCalc['DEGREE_OPERATING_LEV'][year])			
					sectorData['DEGREE_FINANCIAL_LEV'][year].append(dataCalc['DEGREE_FINANCIAL_LEV'][year])			
					sectorData['DFL_RATIO'][year].append(dataCalc['DFL_RATIO'][year]) 					
					sectorData['FINANCIAL_LEVERAGE'][year].append(dataCalc['FINANCIAL_LEVERAGE'][year]) 			
					sectorData['EQUITY_RATIO'][year].append(dataCalc['EQUITY_RATIO'][year]) 				
					sectorData['EQUITY_MULTIPLIER_RATIO_1'][year].append(dataCalc['EQUITY_MULTIPLIER_RATIO_1'][year]) 	
					sectorData['EQUITY_MULTIPLIER_RATIO_2'][year].append(dataCalc['EQUITY_MULTIPLIER_RATIO_2'][year]) 	
					sectorData['NAV'][year].append(dataCalc['NAV'][year]) 							
					sectorData['EFFECTIVE_INT_RATE'][year].append(dataCalc['EFFECTIVE_INT_RATE'][year]) 			
					sectorData['DEBT_COST_CAP'][year].append(dataCalc['DEBT_COST_CAP'][year])				
					sectorData['WACC'][year].append(dataCalc['WACC'][year])							
					sectorData['SALES_TURNOVER'][year].append(dataCalc['SALES_TURNOVER'][year]) 				
					sectorData['DSO'][year].append(dataCalc['DSO'][year]) 							
					sectorData['ASSET_TURNOVER'][year].append(dataCalc['ASSET_TURNOVER'][year])				
					sectorData['ASSET_TURN_RATE'][year].append(dataCalc['ASSET_TURN_RATE'][year])				
					sectorData['LT_ASSET_TURNOVER'][year].append(dataCalc['LT_ASSET_TURNOVER'][year])			
					sectorData['LT_ASSET_TURN_RATE'][year].append(dataCalc['LT_ASSET_TURN_RATE'][year])			
					sectorData['INV_SALES_TURNOVER'][year].append(dataCalc['INV_SALES_TURNOVER'][year])			
					sectorData['DSI'][year].append(dataCalc['DSI'][year])							
					sectorData['INV_COGS_TURNOVER'][year].append(dataCalc['INV_COGS_TURNOVER'][year])			
					sectorData['DIO'][year].append(dataCalc['DIO'][year])							
					sectorData['RECEIVABLES_ACCTS_TURNOVER'][year].append(dataCalc['RECEIVABLES_ACCTS_TURNOVER'][year])	
					sectorData['DRO'][year].append(dataCalc['DRO'][year])							
					sectorData['WORKING_CAP_TURNOVER'][year].append(dataCalc['WORKING_CAP_TURNOVER'][year])			
					sectorData['DWC'][year].append(dataCalc['DWC'][year])							
					sectorData['ROI_INVESTMENTS'][year].append(dataCalc['ROI_INVESTMENTS'][year])				
					sectorData['CREDITORS_TURNOVER'][year].append(dataCalc['CREDITORS_TURNOVER'][year])			
					sectorData['CDO'][year].append(dataCalc['CDO'][year])							
					sectorData['PAYABLES_TURNOVER_COGS'][year].append(dataCalc['PAYABLES_TURNOVER_COGS'][year])		
					sectorData['DPO_COGS'][year].append(dataCalc['DPO_COGS'][year])						
					sectorData['PAYABLES_TURNOVER_COS'][year].append(dataCalc['PAYABLES_TURNOVER_COS'][year])		
					sectorData['DPO_COS'][year].append(dataCalc['DPO_COS'][year])						
					sectorData['LIAB_TURNOVER'][year].append(dataCalc['LIAB_TURNOVER'][year])				
					sectorData['LIAB_TURN_RATE'][year].append(dataCalc['LIAB_TURN_RATE'][year])				
					sectorData['CHG_DEBT_REPAYMENT_REQ'][year].append(dataCalc['CHG_DEBT_REPAYMENT_REQ'][year])		
					sectorData['DEBTORS_PAYBACK_PERIOD'][year]	.append(dataCalc['DEBTORS_PAYBACK_PERIOD'][year])		
					sectorData['BURN_RATE'][year].append(dataCalc['BURN_RATE'][year])					
					sectorData['CCC'][year].append(dataCalc['CCC'][year])							
					sectorData['ROS'][year].append(dataCalc['ROS'][year])							
					sectorData['ROE'][year].append(dataCalc['ROE'][year])							
					sectorData['ROA'][year].append(dataCalc['ROA'][year])							
					sectorData['ROCE_NI'][year].append(dataCalc['ROCE_NI'][year])						
					sectorData['EPS_DILUTED_NI'][year].append(dataCalc['EPS_DILUTED_NI'][year])				
					sectorData['EPS_DILUTED_EBIT'][year].append(dataCalc['EPS_DILUTED_EBIT'][year])				
					sectorData['ROCE_EBIT'][year].append(dataCalc['ROCE_EBIT'][year])					
					sectorData['PE'][year].append(dataCalc['PE'][year])							
					sectorData['PE_REL_3'][year].append(dataCalc['PE_REL_3'][year])						
					sectorData['PE_REL_5'][year].append(dataCalc['PE_REL_5'][year])						
					sectorData['EARNINGS_POWER'][year].append(dataCalc['EARNINGS_POWER'][year])				
					sectorData['GROSS_MARGIN'][year].append(dataCalc['GROSS_MARGIN'][year])					
					sectorData['NOPAT_NI'][year].append(dataCalc['NOPAT_NI'][year])						
					sectorData['NOPAT_EBIT'][year].append(dataCalc['NOPAT_EBIT'][year])					
					sectorData['ROIC'][year].append(dataCalc['ROIC'][year])							
					sectorData['OPERATING_RATIO'][year].append(dataCalc['OPERATING_RATIO'][year])				
					sectorData['OP_PROFIT_MARGIN'][year].append(dataCalc['OP_PROFIT_MARGIN'][year])				
					sectorData['MV'][year].append(dataCalc['MV'][year])							
					sectorData['MV_EBIT_RATIO'][year].append(dataCalc['MV_EBIT_RATIO'][year])				
					sectorData['ORIG_GRAHAM'][year].append(dataCalc['ORIG_GRAHAM'][year])					
					sectorData['REVISED_GRAHAM'][year].append(dataCalc['REVISED_GRAHAM'][year])				
					sectorData['EV'][year].append(dataCalc['EV'][year])							
					sectorData['EV_EBIT'][year].append(dataCalc['EV_EBIT'][year])						
					sectorData['EV_NI'][year].append(dataCalc['EV_NI'][year])						
					sectorData['BV'][year].append(dataCalc['BV'][year])							
					sectorData['BV_PER_SHARE'][year].append(dataCalc['BV_PER_SHARE'][year])					
					sectorData['BV_NI'][year].append(dataCalc['BV_NI'][year])						
					sectorData['BV_EBIT'][year].append(dataCalc['BV_EBIT'][year])						
					sectorData['PRICE_SALES'][year].append(dataCalc['PRICE_SALES'][year])					
					sectorData['PRICE_BOOK'][year].append(dataCalc['PRICE_BOOK'][year])					
					sectorData['PRICE_NAV'][year].append(dataCalc['PRICE_NAV'][year])					
					sectorData['PRICE_FCF'][year].append(dataCalc['PRICE_FCF'][year])					
					sectorData['PRICE_UN_FCF'][year].append(dataCalc['PRICE_UN_FCF'][year])					
					sectorData['MV_OCF'][year].append(dataCalc['MV_OCF'][year])						
					sectorData['CASH_PRICE_RATIO'][year].append(dataCalc['CASH_PRICE_RATIO'][year])				
					sectorData['INTRINSIC_VALUE_NI'][year].append(dataCalc['INTRINSIC_VALUE_NI'][year])			
					sectorData['INTRINSIC_VALUE_EBIT'][year].append(dataCalc['INTRINSIC_VALUE_EBIT'][year])			
					sectorData['INTRINSIC_VALUE_FCF'][year].append(dataCalc['INTRINSIC_VALUE_FCF'][year])			
					sectorData['MARGIN_OF_SAFETY_NI'][year].append(dataCalc['MARGIN_OF_SAFETY_NI'][year])			
					sectorData['MARGIN_OF_SAFETY_EBIT'][year].append(dataCalc['MARGIN_OF_SAFETY_EBIT'][year])		
					sectorData['MARGIN_OF_SAFETY_FCF'][year].append(dataCalc['MARGIN_OF_SAFETY_FCF'][year])			
					sectorData['DUPONT_SYSTEM_1'][year].append(dataCalc['DUPONT_SYSTEM_1'][year])				
					sectorData['RETENTION_RATIO'][year].append(dataCalc['RETENTION_RATIO'][year])				
					sectorData['DIV_PAYOUT_RATIO'][year].append(dataCalc['DIV_PAYOUT_RATIO'][year])				
					sectorData['EARNINGS_YIELD'][year].append(dataCalc['EARNINGS_YIELD'][year])				
					sectorData['DIVS_YIELD'][year].append(dataCalc['DIVS_YIELD'][year])					
					sectorData['SGR'][year].append(dataCalc['SGR'][year])		
					year += 1

		#print(sectorData)
		#print()
		#print()
		#print()
		sectors.append(sectorData)

		sec += 1
		
	return sectors




##def findSector(symbol, sectorList):

#	for sector in sectorList:
#		for company in sector:
#			if(symbol == company):
#				return #sector name

#	return "Sector not found"
