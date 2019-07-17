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
assets = 80
earnings = 10
dividends = 5
retainedEarnings = price - dividends
sectorHighPeMult = 18
sectorLowPwMult = 7
shareholdersEquity = 20
peMult = 8.5
peArray3 = [peMult - 1, peMult, peMult + 1]
peArray5 = [peMult - 1, peMult, peMult + 1, peMult - 1, peMult + 1]
peArray10 = [peMult - 1, peMult, peMult + 1, peMult - 1, peMult, peMult + 1, peMult - 1, peMult, peMult + 1, peMult]
noGrowthPe = 8.5
growthMult = 2
bookValue = 20

# Valuation Formulas
def pe(price, earnings)
    return price / earnings #Also known as pe absolute

def earningsYield(earnings, price)
    return earnings / price #Expected continuing rate of return

def peRelative3 (peArray3)
    return sum(peArray3)/len(peArray3)
def peRelative5 (peArray5)
    return sum(peArray5)/len(peArray5)
def peRelative10 (peArray10)
    return sum(peArray10)/len(peArray10)

def roe(earnings, shareholdersEquity)
    return earnings / shareholdersEquity

def roic(NOPAT, investedCapital)
    return NOPAT / investedCapital

def retentionRatio(retainedEarnings, earnings)
    return retainedEarnings / earnings

def dividendPayoutRatio( dividends, earnings)
    return dividends / earnings

def sgr(roe, dividendPayoutRatio)
    return roe * (1 - dividendPayoutRatio)
#sgr = roe * retentionRatio as well

def retentionRatio(dividendPayoutRatio)
    return 1 - dividendPayoutRatio

def roa (earnings, assets)
    return earnings / assets

def pb(price, bookValue)
    return price / bookValue
#below 1.0 is good, trackings below 3.0

def origGrahamFormula(eps, noGrowthPe, growthMult, g)
    return eps * (noGrowthPe + growthMult * g)

def revisedGrahamFormula(eps, noGrowthPe, growthMult, g, minReturn, y)
    return (eps * (noGrowthPe + growthMult * g) * minReturn) / y

print("The max value is : ", origGrahamFormula)
input("Press any key to exit")
