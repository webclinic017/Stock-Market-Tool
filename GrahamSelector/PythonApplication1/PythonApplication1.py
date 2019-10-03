import readXlsx
import glob

#Creates JSON objets for database:
symbols = glob.glob("*.xlsx")
for symbol in symbols:
	readXlsx.createLocaljsonObj(symbol)



##Indicated Average Future Earnings Power is the single most important factor of intrinsic value
#def avgLowFutureEarnings():
#	return 4.50

#def avgHighFutureEarning():
#	return 5.50

##Contends for the "Quality" of the company
#def fairHighMultiplier(stableEarnings, estGrowthFactor, estDividends):
#	return 16
#def fairLowMultiplier(stableEarnings, estGrowthFactor, estDividends):
#	return 14	

#def intrinsicValue(avgFutureEarnings, fairMultLow, fairMultHigh):
#	estEarningsPower = (avgLowFutureEarnings() + avgHighFutureEarning() ) /2
#	estCapitalizationFactor = (fairLowMultiplier() + fairHighMultiplier() ) / 2
#	return estEarningsPower * estCapitalizationFactor


























#import inspect

#omit = "as_integer_ratio", "conjugate", "fromhex", "hex", "imag", "is_integer", "real"
#def getTickerAttrs():
#	return [x for x in inspect.getmembers(Reported.ticker) if not (x[0].startswith('__') or x[0] in omit) ]
#tickerAttrs = getTickerAttrs()
#tickerAttrsCount = len(getTickerAttrs())

#def returnEmptyAttrs(tickerAttrs):
#	a = []
#	i=0
#	while( i < len(tickerAttrs)):
#		print(tickerAttrs[i][1].shape)
#		i+=1
#	print(len(tickerAttrs))
	#idx = 0
	#for i in tickerAttrs:
	#	if(i[0] == "CASH_PAID_INT"):
	#		print(idx)
	#	idx += 1
#returnEmptyAttrs(tickerAttrs)
