
# Security Analysis is primarily a process of measurement of value in stocks and safety in bonds
# Analytics are applying standards to facts
# Applying those facts, the primary aim is not to profit from projections, but guard against them.
# The purchaser should be prepared to see unsatsifactory earnings during depression periods such that
	# 1) the company's financial strength will carry it unharmed through the setback
	# 2) Average earnings will be enough to justify the bond or stock purchase under recommendation ***Inherint stability***

#MVP1 Indicated Average ***Future Earnings Power*** is the single most important factor of intrinsic value
# Any estimate may easily fall outside expectations as major business factors: volume, price, and cost are largely unpredictable.

def avgHighFutureEarningsPower():
	return 5.50

def avgLowFutureEarningsPower():
	return 4.50

def avgMidFutureEarningsPower(): 
	return (avgLowFutureEarningsPower() + avgHighFutureEarningsPower() ) / 2

#MVP1 ***Capitalization Factor*** Contends for the "Quality" of the company. Perhaps the assets behind the shares
# There remains a doubt when profits develop as anticipated as to whether the capitalization rate was correctly chosen.
# 
expectedStabilityOfEarnings = None
expectedGrowthFactor		= None
expectedDividendPolicy		= None

def estHighCapitalizationFactor():
	return 16

def estLowCapitalizationFactor():
	return 14	

def estMidCapitalizationFactor():
	return (estHighCapitalizationFactor() + estLowCapitalizationFactor() ) / 2

# MVP0 ***Intrinsic Value*** If sound, it is a price that the investor should feel justified in paying, and in having paid, without regard to what the market does thereater
# The investor can be entirely satisfied by the future earnings, dividends, and balance sheet position, even though the market quotation declined and continued disappointingly low.
# ***Experience affirms that price and independently ascertained value converge over time.***
# Weakness stems from lack of precision and of full dependability that are always associated with the calculations of the economic future. 

EarningsPerShare = None
Dividends		 = None
NetCurrentAssets = None
NetAssetValue	 = None



def estHighIntrinsicValue():
	return estHighCapitalizationFactor() * avgHighFutureEarningsPower()

def estLowIntrinsicValue():
	return estLowCapitalizationFactor() * avgLowFutureEarningsPower()

def estMidIntrinsicValue():
	return (estLowIntrinsicValue() + estHighIntrinsicValue() ) / 2


# Intrinsic Value Band is high & low
#Analyst must use good judgement as to whether the value approach should be recognized. *Good vs Bad judgment to use value analysis.
# Fields for Value Analysis:
	# Stable Securities (i.e. utilities)
	# Extreme disparity between price and value. Large margin of safety to absorb uncertainties and diversification is important.
	# Comparative analysis by reliable and useful conclusions of similarly related companies in which a useful preference can be concluded.

# Securities not suited to valuation analysis:
	# Essentially speculative in character - apparent value is dependent on the viscosities of the future. (Undeveloped inventions)
	# High cost or marginal producers which have no earning power.
	# Speculative capialization structure: SeniorSecurities are disproportionately large to CommonStock
	SeniorSecurities	= None
	CommonStock			= None
	# Strong enterprise with an unusually favorable prospect of continual growth. *Favorites* are hard to arithmetic 


print( avgMidFutureEarningsPower() )
print( estMidCapitalizationFactor() )
print( estHighIntrinsicValue() )
print( estMidIntrinsicValue() )
print( estLowIntrinsicValue() )

#The security analyst is on the safest ground when favorable expectations are treated as an 
#*Added reason* for purchase which would not be unsound if based on the past record and present situation

# Quantitative Analysis: *When dependence on qualitative factors, price is often too high.
#	1) Capitalization (structure of debt, preferred, and common stock)
#	2) Earnings and dividends
#	3) Assets and Liabilities
#	4) Operating statistics

# Qualitative Analysis: Often overestimated
#	1) Nature of the business
#	2) Relative Position of the company in the industry
#	3) Physical, Geographic, and operating characteristics
#	4) ***Character of management***
		#Prove: Superior comparative record overtime... 
		#Measured 2x in earnings plus a substantial increment for "good management" => Overvaluation
#	5) Outlook for the unit, industry or business in general
#	6) Inherent stability - Minimizes the risk of new conditions upsetting the calculations, derived from the character of the business


