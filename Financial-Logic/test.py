import sys

#The return on equity ratio measures how efficiently a company is using its equity to generate profit:
    def roe(netIncome, shareholdersEquity):
        print("ROE: " + netIncome / shareholdersEquity)

roe(sys.argv[1], sys.argv[2])
