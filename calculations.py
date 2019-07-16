# Test Data
epsNormalized = sum([7, 8.5, 10])/3
eps = epsNormalized #steady no growth earnings
g = 1.10 # growth rate
minReturn = 0.044
corporateBondRateAAA = 0.0326 #As of 7/8/2019
y = corporateBondRateAAA
# (2*g) growth rate expected over next 7-10 years
NOPAT = 12 #Net operating profit after tax
investedCapital = 30
price = 100
earnings = 10
dividends = 5
retainedEarnings = price - dividends
sectorHighPeMult = 18
sectorLowPwMult = 7
shareholdersEquity = 20

# Formulas
pe = price / earnings
if sectorHighPeMult < pe :
    highPe = True
else:
     highPe = False

if pe < sectorLowPwMult :
    lowPe = True
else:
    lowPe = False

earningsYield = earnings / price #Expected continuing rate of return
peAbsolute = pe

peRelative3 = sum([pe - 1, pe, pe + 1])/ 3
peRelative5 = sum([pe - 1, pe, pe + 1, pe - 1, pe + 1])/ 5
peRelative10 = sum([pe - 1, pe, pe + 1, pe - 1, pe, pe + 1, pe - 1, pe, pe + 1, pe])/ 10

roe = earnings / shareholdersEquity
roic = NOPAT / investedCapital
retentionRatio = retainedEarnings / earnings
dividendPayoutRatio = dividends / earnings
sgr = roe * (1 - dividendPayoutRatio)
#sgr = roe * retentionRatio as well






origGrahamFormula = eps * (8.5 + 2 * g)
revisedGrahamFormula = (eps * (8.5 + 2 * g) * minReturn) / y

print("The max value is : ", origGrahamFormula)
input("Press any key to exit")
