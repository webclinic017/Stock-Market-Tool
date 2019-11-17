import manageJson
import glob
import os
import Enums
import boundings
import getSectors

#Keep the folder clean of previous json files
#files = glob.glob("*.json")
#for file in files:
#	if(files != None):
#		os.remove(file)

symbols = glob.glob("*.xlsx")
i=0
while(i < len(symbols)):
	symbols[i] = symbols[i].strip(".xlsx")
	#manageJson.runJson(symbols[i])
	i += 1

jsonObjs = glob.glob("*.json")
dataList = []
dataCalcList = []
i=0
while(i < len(jsonObjs)):
	if("Calc" not in jsonObjs[i]):
		dataList.append(jsonObjs[i])
	if("Calc" in jsonObjs[i]):
		dataCalcList.append(jsonObjs[i])
	i += 1

if(len(dataList) != len(dataCalcList)):
	print("There has been an error")

#Generate sector data
ratings = {}
sectorList = getSectors.organizeSectors(symbols)
#print(sectorList)
sectorStats = getSectors.makeSectorData(sectorList, dataList, dataCalcList)
#print(sectorStats)

#Generate recommendations
#Turn Calcs into meaningful interpreatations
i=0
while(i < len(dataList)):
	boundings.genRatings(dataList[i], dataCalcList[i])
	i += 1





