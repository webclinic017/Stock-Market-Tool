#*****************************************************
# Test Data
#*****************************************************
epsNormalized = sum([7, 8.5, 10])/3
eps = epsNormalized #steady no growth earnings
g = 1.10 # growth rate
minReturn = 0.044
corporateBondRateAAA = 0.0326 #As of 7/8/2019
aaaReturn = corporateBondRateAAA
# (2*g) growth rate expected over next 7-10 years
NOPAT = 12 #Net operating profit after tax
investedCapital = 30
price = 100
assets = 80
currentAssets = 7
currentLiabilities = 6
netIncome = 10
dividends = 5
retainedEarnings = price - dividends
sectorHighPeMult = 18
sectorLowPwMult = 7
shareholdersEquity = 20
peMult = 8.5
Re = 1 / peMult
peArray3 = [peMult - 1, peMult, peMult + 1]
peArray5 = [peMult - 1, peMult, peMult + 1, peMult - 1, peMult + 1]
peArray10 = [peMult - 1, peMult, peMult + 1, peMult - 1, peMult, peMult + 1, peMult - 1, peMult, peMult + 1, peMult]
noGrowthPe = 8.5
growthMult = 2
#Carrying value on the balance sheet. Assets - accumulated depreciation
bookValue = 20

class Calculations:

    #*****************************************************
    #Data calculations
    #*****************************************************
    #the value of a security or asset as entered in a company's books.
    def bookValue(assets, intangibleAssets, totalLiabilities):
        return (assets - intangibleAssets - totalLiabilities)

    #NOPAT is a company's after-tax operating profit for all investors, including shareholders and debt holders.
    def NOPAT(netIncome, nonOpGainsAftertax, nonOpLossesAftertax, interestExpense):
        return (netIncome - nonOpGainsAftertax + nonOpLossesAftertax + interestExpense)

    def NOPAT2(operatingIncome, taxRate):
        return operatingIncome * (1-taxRate)

    #*****************************************************
    # Valuation Formulas
    #*****************************************************

    #The price-earnings ratio compares a company’s share price to the earnings per share:
    def pe(price, netIncome):
        return price / netIncome #Also known as pe absolute

    #The lower the P/S ratio, the more attractive the investment. he price-to-sales ratio shows how much the market values every dollar of the company's sales. This ratio can be effective in valuing growth stocks that have yet to turn a profit or have suffered a temporary setback.
    def priceSales(price, sales):
        return price / sales

    #The price-to-book ratio compares a company's market value to its book value. A good P/B ratio for one industry might be a poor ratio for another.
    def priceBook(price, bookValue):
        return price / bookValue
    #below 1.0 is good, trackings below 3.0

    def peRelative3 (peArray3):
        return sum(peArray3)/len(peArray3)
    def peRelative5 (peArray5):
        return sum(peArray5)/len(peArray5)
    def peRelative10 (peArray10):
        return sum(peArray10)/len(peArray10)

    # def roe(netIncome, shareholdersEquity):
    #     return netIncome / shareholdersEquity
    #
    # def roa(netIncome, assets):
    #     return netIncome / assets
    def retentionRatio(retainedEarnings, netIncome):
        return retainedEarnings / netIncome

    def payoutRatio(dividends, netIncome):
        return dividends / netIncome

    def earningsYield(netIncome, price):
        return netIncome / price #Expected continuing rate of return

    def origGrahamFormula(eps, noGrowthPe, growthMult, g):
        return eps * (noGrowthPe + growthMult * g)

    def revisedGrahamFormula(eps, noGrowthPe, growthMult, g, minReturn, aaaReturn):
        return (eps * (noGrowthPe + growthMult * g) * minReturn) / aaaReturn

    #*****************************************************
    # Rates of Return
    #*****************************************************

    def roic(NOPAT, investedCapital):
        return NOPAT / investedCapital

    def sgr(roe, dividendPayoutRatio):
        return roe * (1 - dividendPayoutRatio)
    #sgr = roe * retentionRatio as well

    #Cost of investment capital
    def requiredReturn(riskFreeRate, riskCoeff, expeectedReturn):
        return riskFreeRate + riskCoeff * (expeectedReturn - riskFreeRate)

    #necessary return for investment
    def WACC(Re, Rd, equity, debt, taxRate):
        return (equity / (equity + debt)) * Re + (debt / (equity + debt)) * Rd * (1 - taxRate)

    #ROCE is generally used to find out how efficient and profitable a company is from year to year.
    def ROCE(EBIT, assets, currentLiabilities):
        return EBIT / (assets - currentLiabilities)

    def ROCE2(netIncome, assets, currentLiabilities):
        return netIncome/(assets - currentLiabilities)

    #*****************************************************
    #Liquidity Ratios:
    #*****************************************************

    #The cash ratio measures a company’s ability to pay off short-term liabilities with cash and cash equivalents:
    def cashRatio (cashEquivalents, currentLiabilities):
        return cashEquivalents / currentLiabilities

    #The acid-test ratio measures a company’s ability to pay off short-term liabilities with quick assets:
    def acidTest(currentAssets, inventories, currentLiabilities):
        return (currentAssets - inventories) / currentLiabilities

    #The current ratio measures a company’s ability to pay off short-term liabilities with current assets:
    def currentRatio(currentAssets, currentLiabilities):
        return currentAssets / currentLiabilities

    #The operating cash flow ratio is a measure of the number of times a company can pay off current liabilities with the cash generated in a given period:
    def ocfRatio(operatingCashflow, currentLiabilities):
        return operatingCashflow / currentLiabilities

    #*****************************************************
    #Acute Financial Ratios
    #*****************************************************
    def workingCapRatio(currentAssets, currentLiabilities):
        return currentAssets - currentLiabilities

    #DSO days sales outstanding
    def DSO(receivables, netCreditSales, numDays):
        return (receivables / netCreditSales) * numDays

    #The quick ratio is an indicator of a company’s short-term liquidity position and measures a company’s ability to meet its short-term obligations with its most liquid assets.
    def quick(cashEquivalents, marketableSecurities, receivables, currentLiabilities):
        return (cashEquivalents + marketableSecurities + receivables) / currentLiabilities

    def quick2(currentAssets, inventory, prepaidExpenses, currentLiabilities):
        return (currentAssets + inventory + prepaidExpenses) / currentLiabilities

    #*****************************************************
    #Capital Structure Ratios or Leverage Financial Ratios
    #*****************************************************

    #The debt ratio measures the relative amount of a company’s assets that are provided from debt:
    def debtRatio(totalLiabilities, assets):
        return totalLiabilities / assets

    #The debt to equity ratio calculates the weight of total debt and financial liabilities against shareholders equity:
    def debtEquity(totalLiabilities, shareholdersEquity):
        return totalLiabilities / shareholdersEquity

    #The interest coverage ratio determines how easily a company can pay its interest expenses:
    def interestCoverage(operatingIncome, interestExpense):
        return operatingIncome / interestExpense

    #The debt service coverage ratio determines how easily a company can pay its debt obligations:
    def debtServiceCoverage(operatingIncome, totalDebtService):
        return operatingIncome / totalDebtService

    # DCL This ratio can be used to help determine the most optimal level of financial and operating leverage to use in any firm.
    def dCombinedLeverage(percChangeEPS, percChangeSales):
        return percChangeEPS / percChangeSales

    #Operating leverage measures a company’s fixed costs as a percentage of its total costs. It is used to evaluate the breakeven point for a business
    def dOperatingLeverage(percChangeEBIT, percChangeSales):
        return percChangeEBIT / percChangeSales
        #A company with high operating leverage has a large proportion of fixed costs—which means that a substantial increase in sales can lead to outsized changes in profits.
        #A company with low operating leverage has a large proportion of variable costs—which means that it earns a smaller profit on each sale—but does not have to increase sales as much to cover its lower fixed costs.

    #A degree of financial leverage (DFL) is a leverage ratio that measures the sensitivity of a company’s earnings per share (EPS) to fluctuations in its operating income, as a result of changes in its capital structure.
    def dFinancialLeverage(percChangeEPS, percChangeEBIT):
        return percChangeEPS / percChangeEBIT
        #The higher the degree of financial leverage, the more volatile earnings will be.
        #Since interest is usually a fixed expense, leverage magnifies returns and EPS. This is good when operating income is rising, but it can be a problem when operating income is under pressure.
    def dfl(ebit, interest):
        return ebit / (ebit-interest)
        #The higher the DFL, the more volatile earnings per share (EPS) will be. DFL is invaluable in helping a company assess the amount of debt or financial leverage it should opt for in its capital structure


    #*****************************************************
    #Efficiency Ratios
    #*****************************************************

    # The asset turnover ratio measures a company’s ability to generate sales from assets:
    def assetTurnover(sales, assets):
        return sales / assets

    #The inventory turnover ratio measures how many times a company’s inventory is sold and replaced over a given period:
    def inventoryTurnover(cogs, avgInventory):
        return cogs / avgInventory

    #The accounts receivable turnover ratio measures how many times a company can turn receivables into cash over a given period:
    def receivablesTurnover(netCreditSales, avgAccountsReceivable):
        return netCreditSales / avgAccountsReceivable

    #The days sales in inventory ratio measures the average number of days that a company holds onto its inventory before selling it to customers:
    def daysSalesInventory(cogs, avgInventory):
        return avgInventory / cogs * 365

    #*****************************************************
    #Profitability
    #Profitability ratios measure a company’s ability to generate income relative to revenue, balance sheet assets, operating costs, and equity. Common profitability financial ratios include the following:
    #*****************************************************

    #The gross margin ratio compares the gross profit of a company to its net sales to show how much profit a company makes after paying off its cost of goods sold:
    def grossMargin(grossProfit, sales):
        return grossProfit / sales

    #The operating margin ratio compares the operating income of a company to its net sales to determine operating efficiency:
    def operatingMargin(operatingIncome, sales):
        return operatingIncome / sales

    #The return on equity ratio measures how efficiently a company is using its equity to generate profit:
    def roe(netIncome, shareholdersEquity):
        return netIncome / shareholdersEquity

    #The return on assets ratio measures how efficiently a company is using its assets to generate profit:
    def roa(netIncome, assets):
        return netIncome / assets

    #*****************************************************
    #Market Value Ratios
    #Market value ratios are used to evaluate the share price of a company’s stock. Common market value ratios include the following:
    #*****************************************************

    #The book value per share ratio calculates the per share value of a company based on equity available to shareholders:
    def bookValuePs(shareholdersEquity, sharesOutstanding):
        return shareholdersEquity / sharesOutstanding

    #The dividend yield ratio measures the amount of dividends attributed to shareholders relative to the market value per share:
    def divYieldRatio(divsPerShare, price):
        return divsPerShare / price

    #The earnings per share ratio measures the amount of net income earned for each share outstanding:
    def eps(netIncome, sharesOutstanding):
        return netIncome / sharesOutstanding

    #PEG anticipates the one-year earnings growth rate of the stock.
    def peg(pe, g):
        return pe / g

    # def peg(pe, g, y):
    #     return  pe / g)


    #The price-earnings ratio compares a company’s share price to the earnings per share:
    # def pe(price, netIncome):
    #     return price / netIncome #Also known as pe absolute


    #*****************************************************
    #Red Flag Calclations
    #*****************************************************

    #Large discrepancies between P/B ratio and ROE often send up a red flag on companies. Overvalued growth stocks frequently show a combination of low ROE and high P/B ratios. If a company's ROE is growing, its P/B ratio should also be growing.





print("The max value is : ", Calculations.origGrahamFormula(eps, noGrowthPe, growthMult, g))
input("Press any key to exit")
