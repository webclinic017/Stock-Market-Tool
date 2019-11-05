import manageJson
import glob
import os



symbols = glob.glob("*.json")
for symbol in symbols:
	if(symbol != None):
		os.remove(symbol)



symbols = glob.glob("*.xlsx")
i=0

while(i < len(symbols)):
	symbols[i] = symbols[i].strip(".xlsx")
	manageJson.runJson(symbols[i])
