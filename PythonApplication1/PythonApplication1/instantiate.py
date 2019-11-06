import Calcs


def instantiateData():
	data = {}
	data['symbol']					= None
	data['YEAR_INC']				= [None] * 35
	data['REV']						= [None] * 35
	data['SALES_SERV_REV']			= [None] * 35
	data['OTHER_REV']				= [None] * 35
	data['COST_OF_REV']				= [None] * 35
	data['COGS']					= [None] * 35
	data['PROFIT']					= [None] * 35
	data['OTH_PROFIT']				= [None] * 35
	data['OP_EXP']					= [None] * 35
	data['SG_AND_ADMIN']			= [None] * 35
	data['SELL_AND_MARK']			= [None] * 35
	data['GEN_AND_ADMIN']			= [None] * 35
	data['R_AND_D']					= [None] * 35
	data['DEP_AMORT']				= [None] * 35
	data['OTH_OP_EXP']				= [None] * 35
	data['OP_INC_LOSS']				= [None] * 35
	data['NON_OP_INC_LOSS']			= [None] * 35
	data['NET_INT_EXP']				= [None] * 35
	data['INT_EXP']					= [None] * 35
	data['INT_INC']					= [None] * 35
	data['FOREX']					= [None] * 35
	data['AFFILIATES']				= [None] * 35
	data['NON_OP_INC']				= [None] * 35
	data['PRETAX_INCOME']			= [None] * 35
	data['INC_TAX_EXPENSE']			= [None] * 35
	data['CURR_INC_TAX']			= [None] * 35
	data['DEFF_INC_TAX']			= [None] * 35
	data['CONT_OPS']				= [None] * 35
	data['NET_EXTRA1']				= [None] * 35
	data['DISC_OPS']				= [None] * 35
	data['ACCT_CHNG']				= [None] * 35
	data['INCOME_MI']				= [None] * 35
	data['MIN_INTEREST']			= [None] * 35
	data['NI_INC']  				= [None] * 35
	data['PREF_DIVS']				= [None] * 35
	data['OTH_ADJ']					= [None] * 35
	data['NI_AVAIL_COMMON_GAAP']	= [None] * 35
	data['NI_AVAIL_COMMON_ADJ']		= [None] * 35
	data['NET_ABNORMAL']			= [None] * 35
	data['NET_EXTRA2']				= [None] * 35
	data['BASIC_WEIGHT_AVG_SHARES'] = [None] * 35
	data['DIL_WEIGHT_AVG_SHARES']	= [None] * 35
	data['YEAR_BAL']				= [None] * 35
	data['TOTAL_ASSETS1']			= [None] * 35
	data['CASH_EQ_STI']				= [None] * 35
	data['CASH_EQ']					= [None] * 35
	data['ST_INVEST']				= [None] * 35
	data['ACCTS_REC']				= [None] * 35
	data['ACCTS_REC_NET']			= [None] * 35
	data['NOTES_REC_NET']			= [None] * 35
	data['INV']						= [None] * 35
	data['RAW_MAT']					= [None] * 35
	data['WIP']						= [None] * 35
	data['FIN_GOODS'] 				= [None] * 35
	data['OTH_INV']					= [None] * 35
	data['OTH_ST_ASSETS']			= [None] * 35
	data['DERIV_HEDGE_ASSETS1']		= [None] * 35
	data['TAXES_RECIEV']			= [None] * 35
	data['MISC_ST_ASSETS']			= [None] * 35
	data['TOTAL_CURR_ASSETS']		= [None] * 35
	data['PPE_NET']					= [None] * 35
	data['PPE']						= [None] * 35
	data['ACC_DEPREC']				= [None] * 35
	data['LTI_RECEIVABLES']			= [None] * 35
	data['LT_INVEST']				= [None] * 35
	data['OTH_LT_ASSETS']			= [None] * 35
	data['TOTAL_INTANG_ASSETS']		= [None] * 35
	data['GOODWILL']				= [None] * 35
	data['OTH_INTANG_ASSETS']		= [None] * 35
	data['PREPAID_EXP']				= [None] * 35
	data['DEFF_TAX_ASSETS']			= [None] * 35
	data['DERIV_HEDGE_ASSETS2']		= [None] * 35
	data['MISC_ASSETS']				= [None] * 35
	data['TOTAL_NON_CURR_ASSETS']	= [None] * 35
	data['TOTAL_ASSETS2']			= [None] * 35
	data['LIAB_AND_EQUITY1']		= [None] * 35
	data['PAYABLES_ACCRUALS']		= [None] * 35
	data['PAYABLES']				= [None] * 35
	data['ACCRUED_TAXES']			= [None] * 35
	data['INT_DIVS_PAYABLES']		= [None] * 35
	data['OTH_PAYABLES_ACCURALS']	= [None] * 35
	data['ST_DEBT']					= [None] * 35
	data['ST_BORROWINGS']			= [None] * 35
	data['ST_FIN_LEASES']			= [None] * 35
	data['ST_OP_LEASES']			= [None] * 35
	data['CURR_LT_DEBT']			= [None] * 35
	data['OTH_ST_LIAB']				= [None] * 35
	data['DEFF_REV_1']				= [None] * 35
	data['DERIV_HEDGE_1']			= [None] * 35
	data['MISC_ST_LIAB']			= [None] * 35
	data['TOTAL_CURR_LIAB']			= [None] * 35
	data['LT_DEBT']					= [None] * 35
	data['LT_BORROW']				= [None] * 35
	data['LT_FIN_LEASES']			= [None] * 35
	data['LT_OP_LEASES']			= [None] * 35
	data['OTH_LT_LIAB']				= [None] * 35
	data['ACCURED_LIAB']			= [None] * 35
	data['PENSION_LIAB']			= [None] * 35
	data['PENSIONS']				= [None] * 35
	data['OTH_POST_RET_BEN']		= [None] * 35
	data['DEFF_REV_2']				= [None] * 35
	data['DEF_TAX_LIAB']			= [None] * 35
	data['DERIV_HEDGE_2']			= [None] * 35
	data['MISC_LT_LIAB']			= [None] * 35
	data['TOTAL_NON_CURR_LIAB']		= [None] * 35
	data['TOTAL_LIAB']				= [None] * 35
	data['PREF_EQUITY_HYBRID_CAP']	= [None] * 35
	data['SHARE_CAP_APIC']			= [None] * 35
	data['COMMON_STOCK']			= [None] * 35
	data['ADD_PAID_CAP']			= [None] * 35
	data['TREASURY_STOCK']			= [None] * 35
	data['RE']						= [None] * 35
	data['OTH_EQUITY']				= [None] * 35
	data['EQUITY_BEFORE_MIN_INT']	= [None] * 35
	data['MIN_NON_CONTROL_INT']		= [None] * 35
	data['TOTAL_EQUITY']			= [None] * 35
	data['LIAB_AND_EQUITY']			= [None] * 35
	data['YEAR_CF']					= [None] * 35
	data['NI_CF']  					= [None] * 35
	data['DEPRE_AMORT']				= [None] * 35
	data['NON_CASH_ITEMS']			= [None] * 35
	data['STOCK_COMP']				= [None] * 35
	data['DEF_INT_COMP']			= [None] * 35
	data['OTH_NON_CASH_ADJ']		= [None] * 35
	data['CHG_NON_CASH_OP']			= [None] * 35
	data['CREDIT_SALES']			= [None] * 35
	data['CHG_INVENTORIES']			= [None] * 35
	data['CHG_ACCTS_PAYABLE']		= [None] * 35
	data['CHG_OTHER']				= [None] * 35
	data['NET_CASH_DISC_OPS1']		= [None] * 35
	data['CASH_OP_ACT']				= [None] * 35
	data['CASH_INVEST_ACT1']		= [None] * 35
	data['CHG_FIXED_INTANG']		= [None] * 35
	data['DISP_FIXED_INTANG']		= [None] * 35
	data['DISP_FIXED_PROD_ASSETS']	= [None] * 35
	data['DISP_INTANG_ASSETS']		= [None] * 35
	data['ACQ_FIXED_INTANG']		= [None] * 35
	data['ACQ_FIXED_PROD_ASSETS']	= [None] * 35
	data['ACQ_INTANG_ASSETS']		= [None] * 35
	data['NET_CHG_LT_INVEST']		= [None] * 35
	data['DEC_LT_INVEST']			= [None] * 35
	data['INC_LT_INVEST']			= [None] * 35
	data['NET_CASH_ACQ_DIV']		= [None] * 35
	data['CASH_DIVEST']				= [None] * 35
	data['CASH_ACQ_SUBS']			= [None] * 35
	data['CASH_JVS']				= [None] * 35
	data['OTH_INVEST_ACT']			= [None] * 35
	data['NET_CASH_DISC_OPS2']		= [None] * 35
	data['CASH_INVEST']				= [None] * 35
	data['CASH_FIN_ACT1']			= [None] * 35
	data['DIVS_PAID']				= [None] * 35
	data['CASH_REPAY_DEBT']			= [None] * 35
	data['CASH_ST_DEBT']			= [None] * 35
	data['CASH_LT_DEBT']			= [None] * 35
	data['REPAY_LT_DEBT']			= [None] * 35
	data['CASH_REPURCH_EQUITY']		= [None] * 35
	data['INC_CAPITAL_STOCK']		= [None] * 35
	data['DEC_CAPITAL_STOCK']		= [None] * 35
	data['OTH_FIN_ACT']				= [None] * 35
	data['NET_CASH_DISC_OPS3']		= [None] * 35
	data['CASH_FIN_ACT2']			= [None] * 35
	data['EFFECT_FOREX_RATES']		= [None] * 35
	data['NET_CHG_CASH']			= [None] * 35
	data['CASH_PAID_TAXES']			= [None] * 35
	data['CASH_PAID_INT']			= [None] * 35

	return data
	
def instantiateDataCalc(data):
	dataCalc = {}
	dataCalc['symbol'] = data['symbol']
	dataCalc['YEAR_INC'] = data['YEAR_INC']
	dataCalc['YEAR_BAL'] = data['YEAR_BAL']
	dataCalc['YEAR_CF'] = data['YEAR_CF']
	dataCalc['AVG_NI_3YEAR'] = [None] * 35
	dataCalc['AVG_EBIT_3YEAR'] = [None] * 35
	dataCalc['AVG_LEV_FCF_3YEAR'] = [None] * 35
	dataCalc['MARGINAL_TAX_RATE'] = Calcs.Vars.MARGINAL_TAX_RATE
	dataCalc['MARGINAL_TAX_RATE'][0] = "Marginal Corporate Tax Rate (%)"
	dataCalc['FAIR_RETURN_RATE'] = Calcs.Vars.FAIR_RETURN_RATE
	dataCalc['FAIR_RETURN_RATE'][0] = "Graham's Fair Rate of Return"
	dataCalc['NO_GROWTH_PE'] = [None] * 35
	dataCalc['NO_GROWTH_PE'][0] = "No Growth PE"
	dataCalc['REQUIRED_RETURN'] = [None] * 35
	dataCalc['REQUIRED_RETURN'][0] = "Required Rate of Return"
	dataCalc['AAA_BOND_YIELD'] = [None] * 35
	dataCalc['AAA_BOND_YIELD'][0] = "Yield (%) on a AAA Corporate Bond"
	dataCalc['GROWTH_MULTIPLE'] = [None] * 35
	dataCalc['GROWTH_MULTIPLE'][0] = "Growth Multiple Coefficient"
	dataCalc['REV_GROWTH_RATE'] = Calcs.Vars.REV_GROWTH_RATE
	dataCalc['REV_GROWTH_RATE'][0] = "Revenue Growth Rate (%)"
	dataCalc['EBITDA_GROWTH_RATE'] = Calcs.Vars.EBITDA_GROWTH_RATE
	dataCalc['EBITDA_GROWTH_RATE'][0] = "EBITDA Growth Rate (%)"
	dataCalc['EBIT_GROWTH_RATE'] = Calcs.Vars.EBIT_GROWTH_RATE
	dataCalc['EBIT_GROWTH_RATE'][0] = "EBIT Growth Rate (%)"
	dataCalc['NI_GROWTH_RATE'] = Calcs.Vars.NI_GROWTH_RATE
	dataCalc['NI_GROWTH_RATE'][0] = "Net Income Growth Rate (%)"
	dataCalc['EPS_GROWTH_RATE'] = Calcs.Vars.EPS_GROWTH_RATE
	dataCalc['EPS_GROWTH_RATE'][0] = "EPS Growth Rate (%)"
	dataCalc['GROWTH_RATE'] = Calcs.Vars.GROWTH_RATE
	dataCalc['GROWTH_RATE'][0] = "Generic Growth Rate (%)"
	dataCalc['AVG_3YEARS'] = Calcs.Vars.AVG_3YEARS
	dataCalc['AVG_3YEARS'][0] = "3 Year Average"
	dataCalc['AVG_5YEARS'] = Calcs.Vars.AVG_5YEARS
	dataCalc['AVG_5YEARS'][0] = "5 Year Average"
	dataCalc['COST_OF_SALES'] = Calcs.Vars.COST_OF_SALES
	dataCalc['COST_OF_SALES'][0] = "Cost of Sales"
	dataCalc['WORKING_CAPITAL'] = Calcs.Vars.WORKING_CAPITAL
	dataCalc['WORKING_CAPITAL'][0] = "Working Capital"
	dataCalc['CAPITAL_EMPLOYED'] = Calcs.Vars.CAPITAL_EMPLOYED
	dataCalc['CAPITAL_EMPLOYED'][0] = "Capital Employed"
	dataCalc['TOTAL_INVEST'] = Calcs.Vars.TOTAL_INVEST
	dataCalc['TOTAL_INVEST'][0] = "Total Investments"
	dataCalc['TOTAL_DEBT'] = Calcs.Vars.TOTAL_DEBT
	dataCalc['TOTAL_DEBT'][0] = "Total Debt"
	dataCalc['EBITDA'] = Calcs.Vars.EBITDA
	dataCalc['EBITDA'][0] = "Earnings Before Interst, Taxes, Depreciation, and Amortization (EBITDA)"
	dataCalc['EBIAT'] = Calcs.Vars.EBIAT
	dataCalc['EBIAT'][0] = "Earnings Before Interst, Amortization, and Taxes (EBIAT)"
	dataCalc['EBIT'] = Calcs.Vars.EBIT
	dataCalc['EBIT'][0] = "Earnings Before Interest and Taxes (EBIT)"
	dataCalc['CAPEX'] = Calcs.Vars.CAPEX
	dataCalc['CAPEX'][0] = "Capital Expenditures (CAPEX)"
	dataCalc['LEV_FCF'] = Calcs.Vars.LEV_FCF
	dataCalc['LEV_FCF'][0] = "Levered Free Cash Flow (FCF)"
	dataCalc['UN_LEV_FCF'] = Calcs.Vars.UN_LEV_FCF
	dataCalc['UN_LEV_FCF'][0] = "Unlevered Free Cash Flow"
	dataCalc['AVG_RECEIVABLES'] = Calcs.Vars.AVG_RECEIVABLES
	dataCalc['AVG_RECEIVABLES'][0] = "Average Accounts Receivable"
	dataCalc['AVG_PAYABLES_ACCRUALS'] = Calcs.Vars.AVG_PAYABLES_ACCRUALS
	dataCalc['AVG_PAYABLES_ACCRUALS'][0] = "Average Accounts Payable & Accruals"
	dataCalc['AVG_WORKING_CAPITAL'] = Calcs.Vars.AVG_WORKING_CAPITAL
	dataCalc['AVG_WORKING_CAPITAL'][0] = "Average Working Capital"
	dataCalc['AVG_INVENTORY'] = Calcs.Vars.AVG_INVENTORY
	dataCalc['AVG_INVENTORY'][0] = "Average Inventory"
	dataCalc['AVG_INVEST'] = Calcs.Vars.AVG_INVEST
	dataCalc['AVG_INVEST'][0] = "Average Investment Amount"
	dataCalc['AVG_LT_ASSETS'] = Calcs.Vars.AVG_LT_ASSETS
	dataCalc['AVG_LT_ASSETS'][0] = "Average Long Term Assets"
	dataCalc['AVG_ASSETS'] = Calcs.Vars.AVG_ASSETS
	dataCalc['AVG_ASSETS'][0] = "Average Total Assets"
	dataCalc['AVG_LIABILITIES'] = Calcs.Vars.AVG_LIABILITIES
	dataCalc['AVG_LIABILITIES'][0] = "Average Total Liabilities"
	dataCalc['AVG_EQUITY'] = Calcs.Vars.AVG_EQUITY
	dataCalc['AVG_EQUITY'][0] = "Average Equity"
	dataCalc['AVG_DEBT'] = Calcs.Vars.AVG_DEBT
	dataCalc['AVG_DEBT'][0] = "Average Total Debt"
	dataCalc['CASH_RATIO'] = Calcs.Vars.CASH_RATIO
	dataCalc['CASH_RATIO'][0] = "Cash Ratio"	
	dataCalc['CASH_STI_RATIO'] = Calcs.Vars.CASH_STI_RATIO
	dataCalc['CASH_STI_RATIO'][0] = "Liquid Cash Ratio"
	dataCalc['CASH_SERVICE_RATIO'] = Calcs.Vars.CASH_SERVICE_RATIO
	dataCalc['CASH_SERVICE_RATIO'][0] = "Cash Service Ratio"	
	dataCalc['INT_SERVICE_RATIO'] = Calcs.Vars.INT_SERVICE_RATIO
	dataCalc['INT_SERVICE_RATIO'][0] = "Interest Service Ratio"
	dataCalc['CASH_ST_DEBT_RATIO'] = Calcs.Vars.CASH_ST_DEBT_RATIO
	dataCalc['CASH_ST_DEBT_RATIO'][0] = Calcs.Names.CASH_ST_DEBT_RATIO
	dataCalc['ACID_TEST'] = Calcs.Vars.ACID_TEST
	dataCalc['ACID_TEST'][0] = "Acid Test Ratio"
	dataCalc['QUICK_RATIO'] = Calcs.Vars.QUICK_RATIO
	dataCalc['QUICK_RATIO'][0] = "Quick Ratio"
	dataCalc['QUICK_RATIO_2'] = Calcs.Vars.QUICK_RATIO_2
	dataCalc['QUICK_RATIO_2'][0] = "Quick Ratio - Prepaid Expenses"
	dataCalc['CURRENT_RATIO'] = Calcs.Vars.CURRENT_RATIO
	dataCalc['CURRENT_RATIO'][0] = "Current Ratio"
	dataCalc['WORKING_CAP_RATIO'] = Calcs.Vars.WORKING_CAP_RATIO
	dataCalc['WORKING_CAP_RATIO'][0] = "Net Working Capital Ratio"
	dataCalc['DEBT_SERVICE_RATIO'] = Calcs.Vars.DEBT_SERVICE_RATIO
	dataCalc['DEBT_SERVICE_RATIO'][0] = "Debt Service Ratio"	
	dataCalc['NET_DEBT'] = Calcs.Vars.NET_DEBT
	dataCalc['NET_DEBT'][0] = "Net Debt"
	dataCalc['DEBT_RATIO'] = Calcs.Vars.DEBT_RATIO
	dataCalc['DEBT_RATIO'][0] = "Debt Ratio"
	dataCalc['DEBT_EQ_RATIO'] = Calcs.Vars.DEBT_EQ_RATIO
	dataCalc['DEBT_EQ_RATIO'][0] = "Debt to Equity Ratio"
	dataCalc['DEBT_TO_NI'] = Calcs.Vars.DEBT_TO_NI
	dataCalc['DEBT_TO_NI'][0] = "Debt to Income Ratio"
	dataCalc['FIXED_CHARGE_COVERAGE'] = Calcs.Vars.FIXED_CHARGE_COVERAGE
	dataCalc['FIXED_CHARGE_COVERAGE'][0] = "Fixed Charge Coverage"
	dataCalc['DEGREE_COMBINED_LEV'] = Calcs.Vars.DEGREE_COMBINED_LEV
	dataCalc['DEGREE_COMBINED_LEV'][0] = "Degree of Combined Leverage"
	dataCalc['DEGREE_OPERATING_LEV'] = Calcs.Vars.DEGREE_OPERATING_LEV
	dataCalc['DEGREE_OPERATING_LEV'][0] = "Degree of Operating Leverage"
	dataCalc['DEGREE_FINANCIAL_LEV'] = Calcs.Vars.DEGREE_FINANCIAL_LEV
	dataCalc['DEGREE_FINANCIAL_LEV'][0] = "Degree of Financial Leverage"
	dataCalc['DFL_RATIO'] = Calcs.Vars.DFL_RATIO
	dataCalc['DFL_RATIO'][0] = "Degree of Financial Leverage Ratio"
	dataCalc['FINANCIAL_LEVERAGE'] = Calcs.Vars.FINANCIAL_LEVERAGE
	dataCalc['FINANCIAL_LEVERAGE'][0] = "Financial Leverage"
	dataCalc['EQUITY_RATIO'] = Calcs.Vars.EQUITY_RATIO
	dataCalc['EQUITY_RATIO'][0] = "Equity Ratio"
	dataCalc['EQUITY_MULTIPLIER_RATIO_1'] = Calcs.Vars.EQUITY_MULTIPLIER_RATIO_1
	dataCalc['EQUITY_MULTIPLIER_RATIO_1'][0] = "Equity Multiplier"
	dataCalc['EQUITY_MULTIPLIER_RATIO_2'] = Calcs.Vars.EQUITY_MULTIPLIER_RATIO_2
	dataCalc['EQUITY_MULTIPLIER_RATIO_2'][0] = "Equity Multiplier using Debt Ratio"
	dataCalc['NAV'] = Calcs.Vars.NAV
	dataCalc['NAV'][0] = "Net Asset Value"
	dataCalc['EFFECTIVE_INT_RATE'] = Calcs.Vars.EFFECTIVE_INT_RATE
	dataCalc['EFFECTIVE_INT_RATE'][0] = "Effective Interest Rate"
	dataCalc['DEBT_COST_CAP'] = Calcs.Vars.DEBT_COST_CAP
	dataCalc['DEBT_COST_CAP'][0] = "Debt to Cost of Capital"
	dataCalc['WACC'] = Calcs.Vars.WACC
	dataCalc['WACC'][0] = "Weighted Average Cost of Capital (WACC)"
	dataCalc['SALES_TURNOVER'] = Calcs.Vars.SALES_TURNOVER
	dataCalc['SALES_TURNOVER'][0] = "Sales Turnover"
	dataCalc['DSO'] = Calcs.Vars.DSO
	dataCalc['DSO'][0] = "Days Sales Outstanding"
	dataCalc['ASSET_TURNOVER'] = Calcs.Vars.ASSET_TURNOVER
	dataCalc['ASSET_TURNOVER'][0] = "Asset Turnover"
	dataCalc['ASSET_TURN_RATE'] = Calcs.Vars.ASSET_TURN_RATE
	dataCalc['ASSET_TURN_RATE'][0] = "Asset Turnover Rate in Days"
	dataCalc['LT_ASSET_TURNOVER'] = Calcs.Vars.LT_ASSET_TURNOVER
	dataCalc['LT_ASSET_TURNOVER'][0] = "Fixed Asset Turnover"
	dataCalc['LT_ASSET_TURN_RATE'] = Calcs.Vars.LT_ASSET_TURN_RATE
	dataCalc['LT_ASSET_TURN_RATE'][0] = "Fixed Asset Turnover Rate in Days"
	dataCalc['INV_SALES_TURNOVER'] = Calcs.Vars.INV_SALES_TURNOVER
	dataCalc['INV_SALES_TURNOVER'][0] = "Inventory Sales Turnover"
	dataCalc['DSI'] = Calcs.Vars.DSI
	dataCalc['DSI'][0] = "Days Sales Inventory"
	dataCalc['INV_COGS_TURNOVER'] = Calcs.Vars.INV_COGS_TURNOVER
	dataCalc['INV_COGS_TURNOVER'][0] = "Inventory COGS Turnover"
	dataCalc['DIO'] = Calcs.Vars.DIO
	dataCalc['DIO'][0] = "Days Inventory Outstanding"
	dataCalc['RECEIVABLES_ACCTS_TURNOVER'] = Calcs.Vars.RECEIVABLES_ACCTS_TURNOVER
	dataCalc['RECEIVABLES_ACCTS_TURNOVER'][0] = "Accounts Receivables Turnover"
	dataCalc['DRO'] = Calcs.Vars.DRO
	dataCalc['DRO'][0] = "Days Receivables Outstanding"
	dataCalc['WORKING_CAP_TURNOVER'] = Calcs.Vars.WORKING_CAP_TURNOVER
	dataCalc['WORKING_CAP_TURNOVER'][0] = "Working Capital Turnover"
	dataCalc['DWC'] = Calcs.Vars.DWC
	dataCalc['DWC'][0] = "Days Working Capital"
	dataCalc['ROI_INVESTMENTS'] = Calcs.Vars.ROI_INVESTMENTS
	dataCalc['ROI_INVESTMENTS'][0] = "Return on Investments"
	dataCalc['CREDITORS_TURNOVER'] = Calcs.Vars.CREDITORS_TURNOVER
	dataCalc['CREDITORS_TURNOVER'][0] = "Creditors Turnover"
	dataCalc['CDO'] = Calcs.Vars.CDO
	dataCalc['CDO'][0] = "Creditors Days Outstandings"
	dataCalc['PAYABLES_TURNOVER_COGS'] = Calcs.Vars.PAYABLES_TURNOVER_COGS
	dataCalc['PAYABLES_TURNOVER_COGS'][0] = "Payables Turnover using COGS"
	dataCalc['DPO_COGS'] = Calcs.Vars.DPO_COGS
	dataCalc['DPO_COGS'][0] = "Days Payables Outstanding using COGS"
	dataCalc['PAYABLES_TURNOVER_COS'] = Calcs.Vars.PAYABLES_TURNOVER_COS
	dataCalc['PAYABLES_TURNOVER_COS'][0] = "Payables Turnover using Cost of Sales"
	dataCalc['DPO_COS'] = Calcs.Vars.DPO_COS
	dataCalc['DPO_COS'][0] = "Days Payables Outstanding using Cost of Sales"
	dataCalc['LIAB_TURNOVER'] = Calcs.Vars.LIAB_TURNOVER
	dataCalc['LIAB_TURNOVER'][0] = "Liabilities Turnover"
	dataCalc['LIAB_TURN_RATE'] = Calcs.Vars.LIAB_TURN_RATE
	dataCalc['LIAB_TURN_RATE'][0] = "Liabilities Turnover Rate in Days"
	dataCalc['CHG_DEBT_REPAYMENT_REQ'] = Calcs.Vars.CHG_DEBT_REPAYMENT_REQ
	dataCalc['CHG_DEBT_REPAYMENT_REQ'][0] = "Change in Required Short Term Debt Repayments"
	dataCalc['DEBTORS_PAYBACK_PERIOD'] = Calcs.Vars.DEBTORS_PAYBACK_PERIOD
	dataCalc['DEBTORS_PAYBACK_PERIOD'][0] = "Pace of Debt Repayment"
	dataCalc['BURN_RATE'] = Calcs.Vars.BURN_RATE
	dataCalc['BURN_RATE'][0] = "Burn Rate"
	dataCalc['CCC'] = Calcs.Vars.CCC
	dataCalc['CCC'][0] = "Cash Conversion Cycle (CCC)"
	dataCalc['ROS'] = Calcs.Vars.ROS
	dataCalc['ROS'][0] = "Return on Sales"
	dataCalc['ROE'] = Calcs.Vars.ROE
	dataCalc['ROE'][0] = "Return on Equity"
	dataCalc['ROA'] = Calcs.Vars.ROA
	dataCalc['ROA'][0] = "Return on Assets"
	dataCalc['ROCE_NI'] = Calcs.Vars.ROCE_NI
	dataCalc['ROCE_NI'][0] = "Return on Capital Employed (ROCE) using Net Income"
	dataCalc['EPS_DILUTED_NI'] = Calcs.Vars.EPS_DILUTED_NI
	dataCalc['EPS_DILUTED_NI'][0] = "Earnings per Share using Diluted Shares"	
	dataCalc['EPS_DILUTED_EBIT'] = Calcs.Vars.EPS_DILUTED_EBIT
	dataCalc['EPS_DILUTED_EBIT'][0] = "EBIT per Share using Diluted Shares"
	dataCalc['ROCE_EBIT'] = Calcs.Vars.ROCE_EBIT
	dataCalc['ROCE_EBIT'][0] = "Return on Capital Employed using EBIT"
	dataCalc['PE'] = Calcs.Vars.PE
	dataCalc['PE'][0] = "Price to Earnings Ratio (P/E)"
	dataCalc['PE_REL_3'] = Calcs.Vars.PE_REL_3
	dataCalc['PE_REL_3'][0] = "3 Year Average of PE Ratio"
	dataCalc['PE_REL_5'] = Calcs.Vars.PE_REL_5
	dataCalc['PE_REL_5'][0] = "5 Year Average of PE Ratio"
	dataCalc['EARNINGS_POWER'] = Calcs.Vars.EARNINGS_POWER
	dataCalc['EARNINGS_POWER'][0] = "Earnings Power"
	dataCalc['GROSS_MARGIN'] = Calcs.Vars.GROSS_MARGIN
	dataCalc['GROSS_MARGIN'][0] = "Gross Margin"
	dataCalc['NOPAT_NI'] = Calcs.Vars.NOPAT_NI
	dataCalc['NOPAT_NI'][0] = "Net Operating Profit After Tax using Net Income"
	dataCalc['NOPAT_EBIT'] = Calcs.Vars.NOPAT_EBIT
	dataCalc['NOPAT_EBIT'][0] = "Net Operating Profit After Tax using Operating Income"
	dataCalc['ROIC'] = Calcs.Vars.ROIC
	dataCalc['ROIC'][0] = "Return on Invested Capital (ROIC)"
	dataCalc['OPERATING_RATIO'] = Calcs.Vars.OPERATING_RATIO
	dataCalc['OPERATING_RATIO'][0] = "Operating Ratio"
	dataCalc['OP_PROFIT_MARGIN'] = Calcs.Vars.OP_PROFIT_MARGIN
	dataCalc['OP_PROFIT_MARGIN'][0] = "Operating Profit Margin"
	dataCalc['MV'] = Calcs.Vars.MV
	dataCalc['MV'][0] = "Market Value"
	dataCalc['MV_EBIT_RATIO'] = Calcs.Vars.MV_EBIT_RATIO
	dataCalc['MV_EBIT_RATIO'][0] = "Market Value to Cash Flow"
	dataCalc['ORIG_GRAHAM'] = Calcs.Vars.ORIG_GRAHAM
	dataCalc['ORIG_GRAHAM'][0] = "Original Graham Equation"
	dataCalc['REVISED_GRAHAM'] = Calcs.Vars.REVISED_GRAHAM
	dataCalc['REVISED_GRAHAM'][0] = "Revised Graham Equation"
	dataCalc['EV'] = Calcs.Vars.EV
	dataCalc['EV'][0] = "Enterprise Value"
	dataCalc['EV_EBIT'] = Calcs.Vars.EV_EBIT
	dataCalc['EV_EBIT'][0] = "Enterprise Value to Cash Flow"
	dataCalc['EV_NI'] = Calcs.Vars.EV_NI
	dataCalc['EV_NI'][0] = "Enterprise Value to Net Income"
	dataCalc['BV'] = Calcs.Vars.BV
	dataCalc['BV'][0] = "Book Value"
	dataCalc['BV_PER_SHARE'] = Calcs.Vars.BV_PER_SHARE
	dataCalc['BV_PER_SHARE'][0] = "Book Value per Share Outstanding"
	dataCalc['BV_NI'] = Calcs.Vars.BV_NI
	dataCalc['BV_NI'][0] = "Book Value to Net Income per Share"
	dataCalc['BV_EBIT'] = Calcs.Vars.BV_EBIT
	dataCalc['BV_EBIT'][0] = "Book Value to Cash Flow per Share"
	dataCalc['PRICE_SALES'] = Calcs.Vars.PRICE_SALES
	dataCalc['PRICE_SALES'][0] = "Price to Sales Ratio"
	dataCalc['PRICE_BOOK'] = Calcs.Vars.PRICE_BOOK
	dataCalc['PRICE_BOOK'][0] = "Price to Book Ratio"
	dataCalc['PRICE_NAV'] = Calcs.Vars.PRICE_NAV
	dataCalc['PRICE_NAV'][0] = "Price to Net Asset Value"
	dataCalc['PRICE_FCF'] = Calcs.Vars.PRICE_FCF
	dataCalc['PRICE_FCF'][0] = "Price to Free Cash Flow"
	dataCalc['PRICE_UN_FCF'] = Calcs.Vars.PRICE_UN_FCF
	dataCalc['PRICE_UN_FCF'][0] = "Price to UnLevered Free Cash Flow"
	dataCalc['MV_OCF'] = Calcs.Vars.MV_OCF
	dataCalc['MV_OCF'][0] = "Price to Operating Cash Flow"
	dataCalc['CASH_PRICE_RATIO'] = Calcs.Vars.CASH_PRICE_RATIO
	dataCalc['CASH_PRICE_RATIO'][0] = "Cash to Price Ratio"
	dataCalc['INTRINSIC_VALUE_NI'] = Calcs.Vars.INTRINSIC_VALUE_NI
	dataCalc['INTRINSIC_VALUE_NI'][0] = "Intrinsic Value by 3 Year Net Income Average"
	dataCalc['INTRINSIC_VALUE_EBIT'] = Calcs.Vars.INTRINSIC_VALUE_EBIT
	dataCalc['INTRINSIC_VALUE_EBIT'][0] = "Intrinsic Value by 3 Year EBIT Average"
	dataCalc['INTRINSIC_VALUE_FCF'] = Calcs.Vars.INTRINSIC_VALUE_FCF
	dataCalc['INTRINSIC_VALUE_FCF'][0] = "Intrinsic Value by Free Cash Flow"
	dataCalc['MARGIN_OF_SAFETY_NI'] = Calcs.Vars.MARGIN_OF_SAFETY_NI
	dataCalc['MARGIN_OF_SAFETY_NI'][0] = "Margin of Safety by 3 Year Net Income Average"
	dataCalc['MARGIN_OF_SAFETY_EBIT'] = Calcs.Vars.MARGIN_OF_SAFETY_EBIT
	dataCalc['MARGIN_OF_SAFETY_EBIT'][0] = "Margin of Safety by 3 Year EBIT Average"
	dataCalc['MARGIN_OF_SAFETY_FCF'] = Calcs.Vars.MARGIN_OF_SAFETY_FCF
	dataCalc['MARGIN_OF_SAFETY_FCF'][0] = "Margin of Safety by Free Cash Flow"
	dataCalc['DUPONT_SYSTEM_1'] = Calcs.Vars.DUPONT_SYSTEM_1
	dataCalc['DUPONT_SYSTEM_1'][0] = "DuPont System of Valuation Method 1"
	dataCalc['DUPONT_SYSTEM_2'] = Calcs.Vars.DUPONT_SYSTEM_2
	dataCalc['DUPONT_SYSTEM_2'][0] = "DuPont System of Valuation Method 2"
	dataCalc['RETENTION_RATIO'] = Calcs.Vars.RETENTION_RATIO
	dataCalc['RETENTION_RATIO'][0] = "Retention Ratio"
	dataCalc['DIV_PAYOUT_RATIO'] = Calcs.Vars.DIV_PAYOUT_RATIO
	dataCalc['DIV_PAYOUT_RATIO'][0] = "Dividend Payout Ratio"
	dataCalc['EARNINGS_YIELD'] = Calcs.Vars.EARNINGS_YIELD
	dataCalc['EARNINGS_YIELD'][0] = "Earnings Yield Ratio"
	dataCalc['DIVS_YIELD'] = Calcs.Vars.DIVS_YIELD
	dataCalc['DIVS_YIELD'][0] = "Dividends Yield Ratio"
	dataCalc['SGR'] = Calcs.Vars.SGR
	dataCalc['SGR'][0] = "Sustainable Growth Rate"

	return dataCalc
