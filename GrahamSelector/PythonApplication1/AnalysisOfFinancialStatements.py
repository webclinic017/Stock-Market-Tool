#************************************************
#Qualitative Analysis:
#************************************************

#Description of the company's business and properties. 
#Historical information about the details of management

#1) Prospectus: Issuances of new securirity offerings
	#Describes factors for which may make larger or smaller profits in the future.
#2) Reports on investment services: Credit bureaus 



#************************************************
#Income Statement Analysis:
#************************************************

#major criteria of the position of a security.

#Coverage (Stability): the number of times fixed charges (plus preferred dividends) have been earned.
#Earnings per share of the common stock.

#Various perspectives of using historical data: to determine earning power.
#1) Average results per period
#2) Minimum for any year
#3) Trend over the years
#--------
#4) "Excessive" importance paid to the current figure.
#5) "Discernment" must weigh the importance of published figures.

#Headings:
#A) Accounting: What are the true ("Oridinary Earnings") earnings for the period studied?
	#1) Eliminate non-recurring items from a single-year analysis. Include most of them in the long-term analysis.
		#past years:
			#1) Payments of back taxes or tax refunds not previously provided for and interest that may be accompanied by adjustments in depreciation reserves
			#2) Payments as a result of litigation and other claims relating to prior years.
			#3) Profit or loss of a sale of a fixed asset.
			
			#Schools of thought:
			#A) All inclusive-includes them,  remove those which do not reflect operating results

			# => ***Take every real profit or loss item unless unrelated to the normal operations of the business.***
				#Small items < 10% of aggregate are included
				#When excluding a large item, adjust the income tax deduction.
#Example:
DeGiogio_NI = 2444
SaleOfCapitalAssets = 2735
taxRate = 0.25

if(SaleOfCapitalAssets > (0.1 * DeGiogio_NI) ):
	NetSaleOfCapitalAssets = SaleOfCapitalAssets * (1 - taxRate)
	NI_Adj = DeGiogio_NI - NetSaleOfCapitalAssets
else:
	NI_Adj = DeGiogio_NI

#print(NI_Adj)

			#4) adjustments of market value, a write down of nonmarketable investments
			#5) write downs or recoveries of foreign assets
			#6) proceeds of life insurance policies collected.
			#7) chargeoffs in connection with bond retirements and new financing.


	#2) Exclude deductions or credits arising from the use of contingency and other arbitrary reserves.
	#3) Place the depreciation & amortization allowance and inventory valuation on a suitable basis for comparative study
	#4) Adjust earnings for operations of subsidiaries and affialiates to the extent they are not shown.
	#5) As a check, Reconcile the alloances for federal income tax with reported earnings.


#B) Business: What indications does the earnings record carry as the future earning power of the company?
#C) Security valuation: What eleemnts in the earnings exhibit must be taken into account, what standards followed, in endeavoring to arrive at a reasonable valuation of shares









































#************************************************
#Balance Sheet Analysis:
#************************************************
