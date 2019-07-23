

netIncome = 10
shareholdersEquity = 30
assets = 100

class Calculations:

    #The return on equity ratio measures how efficiently a company is using its equity to generate profit:
    def roe(netIncome, shareholdersEquity):
        return netIncome / shareholdersEquity

    #The return on assets ratio measures how efficiently a company is using its assets to generate profit:
    def roa(netIncome, assets):
        return netIncome / assets


print("ROE: ", Calculations.roe(netIncome, shareholdersEquity))
print("ROA: ", Calculations.roa(netIncome, assets))
input("Press any key to exit")
